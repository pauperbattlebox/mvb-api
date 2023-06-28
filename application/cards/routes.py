from flask import Blueprint, abort
from flask import current_app as app
from flask import jsonify, redirect, request
from marshmallow.exceptions import ValidationError

from application import cache, current_version, limiter
from application.models import Cards, Meta, Prices
from application.repositories.card_repository import *
from application.schemas import (
    card_schema,
    card_with_related_printings_schema,
    cards_schema,
    cardssearchschema,
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

    q = get_cards_by_attribue(args)

    result = cards_schema.dump(q)

    return jsonify(result)


################# GET SINGLE CARD ############################
####GET CARD BY CS ID
@cards.route(current_version + "/cards/cs/<cs_id>")
@limiter.limit("120/minute")
@cache.cached(timeout=86400, query_string=True)
def get_by_cs_id(cs_id):
    args = request.args

    q = get_card_by_cs_id(cs_id)

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


####GET CARDS BY MTGJSON ID
@cards.route(current_version + "/cards/mtgjson/<mtgjson_id>")
@limiter.limit("120/minute")
@cache.cached(timeout=86400)
def get_by_mtgjson_id(mtgjson_id):

    q = get_cards_by_mtgjson_id(mtgjson_id)

    result = cards_schema.dump(q)

    return jsonify(result)


####GET CARD BY SCRYFALL ID
@cards.route(current_version + "/cards/scryfall/<scryfall_id>")
@limiter.limit("120/minute")
@cache.cached(timeout=86400)
def get_by_scryfall_id(scryfall_id):

    q = get_cards_by_scryfall_id(scryfall_id)

    result = cards_schema.dump(q)

    return jsonify(result)
