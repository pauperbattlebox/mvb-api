from flask import Blueprint, jsonify
from flask import current_app as app

from application.models import Cards
from application.schemas import card_schema, cards_schema

from application import current_version

cards = Blueprint('cards', __name__)


################ GET MULTIPLE CARDS ###########################
####GET CARDS BY CS CARD NAME
@cards.route(current_version + 'cards/name/<card_name>')
def get_by_card_name(card_name):

    q = Cards.query.filter(Cards.name == card_name).all()

    result = cards_schema.dump(q)

    return jsonify(result)


####SEARCH BY CARD NAME
@cards.route(current_version + 'cards/search/<card_name>')
def search_by_card_name(card_name):

    q = Cards.query.filter(Cards.name.match('%' + card_name + '%')).all()

    result = cards_schema.dump(q)

    return jsonify(result)


####GET ALL CARDS IN A CS SET
@cards.route(current_version + '/cards/set/<cs_set>')
def get_by_set(cs_set):

    q = Cards.query.filter(Cards.edition == cs_set).order_by(Cards.name.asc(), Cards.is_foil.asc()).all()

    result = cards_schema.dump(q)

    return jsonify(result)


################# GET SINGLE CARD ############################
####GET CARD BY CS ID
@cards.route(current_version + '/cards/cardsphere/<cs_id>')
def get_by_cs_id(cs_id):

    q = Cards.query.filter(Cards.cs_id == cs_id).first_or_404()

    result = card_schema.dump(q)

    return jsonify(result)


####GET CARD BY MTGJSON ID
@cards.route(current_version + '/cards/mtgjson/<mtgjson_id>')
def get_by_mtgjson_id(mtgjson_id):

    q = Cards.query.filter(Cards.mtgjson_id == mtgjson_id).first_or_404()

    result = card_schema.dump(q)

    return jsonify(result)



####GET CARD BY SCRYFALL ID
@cards.route(current_version + '/cards/sryfall/<scryfall_id>')
def get_by_scryfall_id(scryfall_id):

    q = Cards.query.filter(Cards.scryfall_id == scryfall_id).first_or_404()

    result = card_schema.dump(q)

    return jsonify(result)


####GET CARD BY SET NAME AND CARD NAME
@cards.route(current_version + '/cards/<set_name>/<card_name>')
def get_by_set_and_name(set_name, card_name):

    q = Cards.query.filter(Cards.edition == set_name, Cards.name == card_name).all()

    result = cards_schema.dump(q)

    return jsonify(result)

####GET CARD BY SET CODE AND CARD NAME
@cards.route(current_version + '/cards/<set_code>/<card_name>')
def get_by_set_code_and_name(set_code, card_name):

    q = Cards.query.filter(Cards.mtgjson_code == set_code, Cards.name == card_name).all()

    result = cards_schema.dump(q)

    return jsonify(result)
