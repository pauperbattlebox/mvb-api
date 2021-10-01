from flask import Blueprint, jsonify
from flask import current_app as app

from application.models import Sets
from application.schemas import set_schema, sets_schema

from application import current_version

sets = Blueprint('sets', __name__)


###GET ALL SETS
@sets.route(current_version + '/sets')
def get_all_sets():

    q = Sets.query.all()

    result = sets_schema.dump(q)

    return jsonify(result)


###GET SET BY CS NAME
@sets.route(current_version + '/sets/<set_name>')
def get_set_by_set_name(set_name):

    q = Sets.query.filter(Sets.cs_name == set_name).first_or_404()

    result = set_schema.dump(q)

    return jsonify(result)


####GET SET BY MTGJSON CODE
####THIS MATCHES *.json file
@sets.route(current_version + '/sets/mtgjsoncode/<mtgjson_code>')
def get_set_by_mtgjson_code(mtgjson_code):

    q = Sets.query.filter(Sets.mtgjson_code == mtgjson_code).first_or_404()

    result = set_schema.dump(q)

    return jsonify(result)
