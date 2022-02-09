from flask import Blueprint
from flask import current_app as app
from flask import render_template

from application import current_version

core = Blueprint('core', __name__)

@core.route('/')
def home():
    return render_template("index.html")


####AUTHENTICATE
