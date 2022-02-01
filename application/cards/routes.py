from flask import Blueprint, jsonify, request, abort
from flask import current_app as app
from marshmallow.exceptions import ValidationError

from application.models import Cards, Prices, Meta
from application.schemas import card_schema, cards_schema, card_with_related_printings_schema, meta_schema, cardssearchschema
from application import current_version, cache, limiter

cards = Blueprint('cards', __name__)

####GET CACHE LAST UPDATED TIMESTAMP
@cards.route(current_version + 'cache')
@limiter.limit("100/minute")
def get_cache():

    q = Meta.query.with_entities(Meta.last_updated).order_by(Meta.last_updated.desc()).first_or_404()

    result = meta_schema.dump(q)

    return jsonify(result)


################ GET MULTIPLE CARDS ###########################
####GET ALL CARDS
@cards.route(current_version + 'cards/all')
@limiter.limit("5/hour")
@cache.cached(timeout=86400)
def get_all_ids():

    q = Meta.query.order_by(Meta.last_updated.desc()).first_or_404()

    result = meta_schema.dump(q)

    p = Cards.query.with_entities(Cards.cs_id, Cards.mtgjson_id, Cards.scryfall_id).all()

    result['cards'] = cards_schema.dump(p)

    return jsonify(result)


####SEARCH BY CARD NAME
@cards.route(current_version + 'cards/search')
@limiter.limit("25/minute")
def search_by_card_name():

    try:
        args = cardssearchschema.load(request.args)

    except ValidationError as e:
        abort(400, e.messages)

    filtered_args = dict()

    for (k, v) in args.items():
        if v and k != 'name':
            filtered_args[k] = v

    q = Cards.query

    if 'name' in args and args['name'] != None:

        search = f"%{args['name']}%"
        q = q.filter(Cards.name.ilike(search))

    q = q.filter_by(**filtered_args).all()

    result = cards_schema.dump(q)

    return jsonify(result)


################# GET SINGLE CARD ############################
####GET CARD BY CS ID
@cards.route(current_version + '/cards/<cs_id>')
@limiter.limit("50/minute")
@cache.cached(timeout=86400)
def get_by_cs_id(cs_id):
    args = request.args

    q = Cards.query.filter(Cards.cs_id == cs_id).first_or_404()

    result = card_with_related_printings_schema.dump(q)

    if 'includeRelatedPrintings' in args and args.get('includeRelatedPrintings').lower() == 'true':

        rp = Cards.query.filter(Cards.name == result['name'], Cards.cs_id != result['cs_id']).order_by(Cards.edition.asc(), Cards.is_foil.asc()).all()

        if len(rp) > 0:
            result['related_printings'] = cards_schema.dump(rp)

    return jsonify(result)


####GET CARDS BY MTGJSON CODE
@cards.route(current_version + '/cards/mtgjson/<mtgjson_code>')
@limiter.limit("50/minute")
@cache.cached(timeout=86400)
def get_by_mtgjson_code(mtgjson_code):

    q = Cards.query.filter(Cards.mtgjson_code == mtgjson_code).all()

    result = cards_schema.dump(q)

    return jsonify(result)


####GET CARD BY MTGJSON ID
@cards.route(current_version + '/cards/mtgjsonid/<mtgjson_id>')
@limiter.limit("100/minute")
@cache.cached(timeout=86400)
def get_by_mtgjson_id(mtgjson_id):

    q = Cards.query.filter(Cards.mtgjson_id == mtgjson_id).first_or_404()

    result = card_schema.dump(q)

    return jsonify(result)


####GET CARD BY SCRYFALL ID
@cards.route(current_version + '/cards/scryfallid/<scryfall_id>')
@limiter.limit("100/minute")
@cache.cached(timeout=86400)
def get_by_scryfall_id(scryfall_id):

    q = Cards.query.filter(Cards.scryfall_id == scryfall_id).first_or_404()

    result = card_schema.dump(q)

    return jsonify(result)
