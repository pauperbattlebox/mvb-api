from flask import Blueprint, jsonify, request
from flask import current_app as app

from application.models import Cards, Prices
from application.schemas import card_schema, cards_schema, card_with_related_printings_schema

from application import current_version, cache

cards = Blueprint('cards', __name__)


################ GET MULTIPLE CARDS ###########################
####SEARCH BY CARD NAME
@cards.route(current_version + 'cards/search/<card_name>')
def search_by_card_name(card_name):

    search = f"%{card_name}%"

    q = Cards.query.filter(Cards.name.ilike(search)).all()

    result = cards_schema.dump(q)

    return jsonify(result)


@cards.route(current_version + 'cards/all')
@cache.cached(timeout=30)
def get_all_ids():

    q = Cards.query.with_entities(Cards.cs_id, Cards.mtgjson_id, Cards.scryfall_id).all()

    result = cards_schema.dump(q)

    return jsonify(result)


################# GET SINGLE CARD ############################
####GET CARD BY CS ID
@cards.route(current_version + '/cards/<cs_id>')
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
def get_by_mtgjson_code(mtgjson_code):

    q = Cards.query.filter(Cards.mtgjson_code == mtgjson_code).all()

    result = cards_schema.dump(q)

    return jsonify(result)


####GET CARD BY MTGJSON ID
@cards.route(current_version + '/cards/mtgjsonid/<mtgjson_id>')
@cache.cached(timeout=0)
def get_by_mtgjson_id(mtgjson_id):

    q = Cards.query.filter(Cards.mtgjson_id == mtgjson_id).first_or_404()

    result = card_schema.dump(q)

    return jsonify(result)



####GET CARD BY SCRYFALL ID
@cards.route(current_version + '/cards/scryfallid/<scryfall_id>')
@cache.cached(timeout=0)
def get_by_scryfall_id(scryfall_id):

    q = Cards.query.filter(Cards.scryfall_id == scryfall_id).first_or_404()

    result = card_schema.dump(q)

    return jsonify(result)
