from flask import Blueprint, jsonify
from flask import current_app as app

from application.models import Cards
from application.schemas import card_schema, cards_schema

cards = Blueprint('cards', __name__)

@cards.route('/cards/<card_name>')
def get_by_card_name(card_name):

    q = Cards.query.filter(Cards.name == card_name).all()

    result = cards_schema.dump(q)

    return jsonify(result)
