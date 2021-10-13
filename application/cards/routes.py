from flask import Blueprint, jsonify
from flask import current_app as app

from application.models import Cards
from application.schemas import card_schema, cards_schema, card_with_related_printings_schema

from application import current_version

cards = Blueprint('cards', __name__)


################ GET MULTIPLE CARDS ###########################
####SEARCH BY CARD NAME
@cards.route(current_version + 'cards/search/<card_name>')
def search_by_card_name(card_name):

    q = Cards.query.filter(Cards.name.match('%' + card_name + '%')).all()

    result = cards_schema.dump(q)

    return jsonify(result)


################# GET SINGLE CARD ############################
####GET CARD BY CS ID
@cards.route(current_version + '/cards/<cs_id>')
def get_by_cs_id(cs_id):
    r = request.args.get('includeRelatedPrintings', None)
    q = Cards.query.filter(Cards.cs_id == cs_id).first_or_404()
    result = card_with_related_printings_schema.dump(q)

    if r is not None:
        rp = Cards.query.filter(Cards.name.match(result.card_name) & Cards.cs_id != result.cs_id).all()

    if rp is not None:
        result.related_printings = cards_schema.dump(rp)    

    return jsonify(result)


####GET CARD BY MTGJSON ID
@cards.route(current_version + '/cards/mtgjson/<mtgjson_id>')
def get_by_mtgjson_id(mtgjson_id):

    q = Cards.query.filter(Cards.mtgjson_id == mtgjson_id).first_or_404()

    result = card_schema.dump(q)

    return jsonify(result)



####GET CARD BY SCRYFALL ID
@cards.route(current_version + '/cards/scryfall/<scryfall_id>')
def get_by_scryfall_id(scryfall_id):

    q = Cards.query.filter(Cards.scryfall_id == scryfall_id).first_or_404()

    result = card_schema.dump(q)

    return jsonify(result)
