from flask import Blueprint, abort
from flask import current_app as app
from flask import jsonify, redirect, request
from marshmallow.exceptions import ValidationError

from application import cache, current_version, limiter
from application.models import Cards, Meta, Prices
from application.schemas import (
    card_schema,
    card_with_related_printings_schema,
    cards_schema,
    cardssearchschema,
    discordsearchschema,
    meta_schema,
)

cards = Blueprint("cards", __name__)

####GET CACHE LAST UPDATED TIMESTAMP
@cards.route(current_version + "cache")
@limiter.limit("100/minute")
def get_cache():

    q = (
        Meta.query.with_entities(Meta.last_updated)
        .order_by(Meta.last_updated.desc())
        .first_or_404()
    )

    result = meta_schema.dump(q)

    return jsonify(result)


################ GET MULTIPLE CARDS ###########################
####GET ALL CARDS
@cards.route(current_version + "cards")
@limiter.limit("5/hour")
def get_all_ids():

    return redirect("https://cdn.multiversebridge.com/all_ids.json", code=302)


####SEARCH BY CARD NAME
@cards.route(current_version + "cards/search")
@limiter.limit("120/minute")
def search_by_card_name():

    if not request.args:
        abort(400, "Please enter at least one query parameter")

    try:
        args = cardssearchschema.load(request.args)

    except ValidationError as e:
        abort(400, e.messages)

    filtered_args = dict()

    for (k, v) in args.items():
        if v and k != "name" and k != "is_foil":
            filtered_args[k] = v

    q = Cards.query

    if "name" in args and args["name"] != None:

        search_term = args["name"]
        search = f"%{search_term}%"
        q = q.filter(Cards.name.ilike(search))

    if "is_foil" in args and args["is_foil"] != None:
        q = q.filter(Cards.is_foil == args["is_foil"])

    q = q.filter_by(**filtered_args).limit(100)

    q.all()

    result = cards_schema.dump(q)

    return jsonify(result)


################# GET SINGLE CARD ############################
####GET CARD BY CS ID
@cards.route(current_version + "/cards/cs/<cs_id>")
@limiter.limit("120/minute")
@cache.cached(timeout=86400, query_string=True)
def get_by_cs_id(cs_id):
    args = request.args

    q = Cards.query.filter(Cards.cs_id == cs_id).first_or_404()

    result = card_with_related_printings_schema.dump(q)

    if (
        "includeRelatedPrintings" in args
        and args.get("includeRelatedPrintings").lower() == "true"
    ):

        rp = (
            Cards.query.filter(
                Cards.name == result["name"], Cards.cs_id != result["cs_id"]
            )
            .order_by(Cards.edition.asc(), Cards.is_foil.asc())
            .all()
        )

        if len(rp) > 0:
            result["related_printings"] = cards_schema.dump(rp)

    return jsonify(result)


####GET CARD BY MTGJSON ID
@cards.route(current_version + "/cards/mtgjson/<mtgjson_id>")
@limiter.limit("120/minute")
@cache.cached(timeout=86400)
def get_by_mtgjson_id(mtgjson_id):

    q = Cards.query.filter(Cards.mtgjson_id == mtgjson_id).all()

    result = cards_schema.dump(q)

    return jsonify(result)


####GET CARD BY SCRYFALL ID
@cards.route(current_version + "/cards/scryfall/<scryfall_id>")
@limiter.limit("120/minute")
@cache.cached(timeout=86400)
def get_by_scryfall_id(scryfall_id):

    q = Cards.query.filter(Cards.scryfall_id == scryfall_id).all()

    result = cards_schema.dump(q)

    return jsonify(result)


####GET CARD BY NAME, CHEAPEAST PRICE
@cards.route(current_version + "/cards/cheapest/<card_name>")
@limiter.limit("120/minute")
@cache.cached(timeout=86400)
def get_cheapest_card(card_name):

    q = (
        Cards.query.join(Cards.prices)
        .with_entities(Prices.price)
        .filter(Cards.name == card_name)
        .order_by(Prices.price.asc())
        .first_or_404()
    )

    return str(q[0])


####DISCORD BOT ROUTES
####GET CS ID BY CARD NAME AND MTGJSON IF INCLUDED
@cards.route(current_version + "/discord/cards/search")
@limiter.limit("120/minute")
def discord_search_by_card_name():

    if not request.args or "name" not in request.args or request.args["name"] == "":
        abort(400, "name missing")

    print(request.args)

    try:
        args = discordsearchschema.load(request.args)

    except ValidationError as e:
        abort(400, e.messages)

    q = Cards.query.with_entities(Cards.cs_id)

    if "name" in args and args["name"] != None:

        search_term = args["name"]
        search = f"%{search_term}%"
        q = q.filter(Cards.name.ilike(search))

    if "mtgjson_code" in args and args["mtgjson_code"] != None:

        args_mtgjson_code = args["mtgjson_code"]

        q = q.filter(Cards.mtgjson_code == args_mtgjson_code)

    q = q.first_or_404()

    result = card_schema.dump(q)

    return jsonify(result)


####GET CARD PRICES BY NAME
@cards.route(current_version + "/discord/cards/price/<card_name>")
@limiter.limit("120/minute")
def get_prices_by_card_name(card_name):

    q = (
        Cards.query.join(Cards.prices)
        .with_entities(Cards.edition, Cards.name, Cards.is_foil, Prices.price)
        .filter(Cards.name.ilike(f"%{card_name}%"))
        .limit(10)
        .all()
    )

    if len(q) <= 0:
        abort(404)

    result = []

    for i in q:
        temp_dict = dict()

        if i.is_foil == True:
            temp_dict["name"] = i.name
            temp_dict["edition"] = i.edition
            temp_dict["price"] = f"${str(round((i[3]), 2))}" + " - FOIL"

            result.append(temp_dict)

        else:
            temp_dict["name"] = i.name
            temp_dict["edition"] = i.edition
            temp_dict["price"] = f"${str(round((i[3]), 2))}"

            result.append(temp_dict)

    return jsonify(result)
