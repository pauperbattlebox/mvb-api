from flask import Blueprint
from flask import current_app as app

core = Blueprint('core', __name__)

@core.route('/')
def home():
    return ("Hello world")


###AUTHENTICATE ROUTE
