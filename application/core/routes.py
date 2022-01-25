from flask import Blueprint, render_template
from flask import current_app as app

from application import current_version

core = Blueprint('core', __name__)

@core.route('/')
def home():
    return render_template("index.html")


####AUTHENTICATE
