from flask import Blueprint, jsonify
from flask import current_app as app

from application.models import Sets
from application.schemas import SetsSchema

sets = Blueprint('sets', __name__)


###GET ALL SETS
@sets.route('/sets')
def get_all_sets():

    sets_schema = SetsSchema(many=True)

    q = Sets.query.all()
    print(q)

    result = sets_schema.dump(q)
    return result


###GET SET BY CS NAME
@sets.route('/sets/<set_name>')
def get_set_by_set_name(set_name):

    return set_name
