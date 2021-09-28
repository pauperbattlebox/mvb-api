from flask import Blueprint, jsonify
from flask import current_app as app

from application.models import Cards
from application.schemas import card_schema, cards_schema

cards = Blueprint('cards', __name__)

####GET CARDS BY CARD NAME
@cards.route('/cards/<card_name>')
def get_by_card_name(card_name):

    q = Cards.query.filter(Cards.name == card_name).all()

    result = cards_schema.dump(q)

    return jsonify(result)


####GET CARD BY CS ID
@cards.route('/cards/csid/<cs_id>')
def get_by_cs_id(cs_id):

    q = Cards.query.filter(Cards.cs_id == cs_id).first_or_404()

    result = card_schema.dump(q)

    return jsonify(result)


####GET CARD BY MTGJSON ID
@cards.route('/cards/mtgjsonid/<mtgjson_id>')
def get_by_mtgjson_id(mtgjson_id):

    q = Cards.query.filter(Cards.mtgjson_id == mtgjson_id).first_or_404()

    result = card_schema.dump(q)

    return jsonify(result)



####GET CARD BY SCRYFALL ID
