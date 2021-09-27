from flask import Blueprint
from flask import current_app as app

sets = Blueprint('sets', __name__)


###GET ALL SETS
@sets.route('/sets')
def get_all_sets():

    return ("All sets")


###GET SET BY CS NAME
@sets.route('/sets/<set_name>')
def get_set_by_set_name(set_name):

    return set_name
