from flask import Blueprint
from flask import current_app as app
from flask import render_template, send_file

core = Blueprint("core", __name__)


@core.route("/")
def home():
    return render_template("index.html")


@core.route("/postman")
def postman():
    return send_file("static/MVB.postman_collection.json", as_attachment=True)
