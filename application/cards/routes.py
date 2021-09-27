from flask import Blueprint
from flask import current_app as app

cards = Blueprint('cards', __name__)

@cards.route('/cards/<card_name>')
def get_by_card_name(card_name):

    return card_name
