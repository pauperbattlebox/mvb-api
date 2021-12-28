from flask import Blueprint, jsonify
from flask import current_app as app

from application.models import Sets, Cards
from application.schemas import sets_schema, set_with_cards_schema, cards_schema

from application import current_version

sets = Blueprint('sets', __name__)


###GET ALL SETS
@sets.route(current_version + '/sets')
def get_all_sets():

    q = Sets.query.all()

    result = sets_schema.dump(q)

    return jsonify(result)


###GET SET BY CS ID
@sets.route(current_version + '/sets/<cs_id>')
def get_set_by_set_name(cs_id):

    q = Sets.query.filter(Sets.cs_id == cs_id).first_or_404()
    result = set_with_cards_schema.dump(q)

    p = Cards.query.filter(Cards.edition == result['cs_name']).order_by(Cards.name.asc(), Cards.is_foil.asc()).all()
    result['cards'] = cards_schema.dump(p)

    return jsonify(result)


####GET SET BY MTGJSON CODE
####THIS MATCHES *.json file
@sets.route(current_version + '/sets/mtgjson/<mtgjson_code>')
def get_set_by_mtgjson_code(mtgjson_code):

    q = Sets.query.filter(Sets.mtgjson_code == mtgjson_code).first_or_404()

    result = set_with_cards_schema.dump(q)

    p = Cards.query.filter(Cards.edition == result['cs_name']).order_by(Cards.name.asc(), Cards.is_foil.asc()).all()

    result['cards'] = cards_schema.dump(p)

    return jsonify(result)
