from flask import Blueprint, jsonify
from flask import current_app as app

from application.models import Sets
from application.schemas import set_schema, sets_schema

sets = Blueprint('sets', __name__)


###GET ALL SETS
@sets.route('/sets')
def get_all_sets():

    q = Sets.query.all()
    print(q)

    result = sets_schema.dump(q)
    return jsonify(result)


###GET SET BY CS NAME
@sets.route('/sets/<set_name>')
def get_set_by_set_name(set_name):

    return set_name
####GET SET BY MTGJSON CODE
####THIS MATCHES *.json file
@sets.route('/sets/<mtgjson_code>')
def get_set_by_mtgjson_code(mtgjson_code):

    return set_name
