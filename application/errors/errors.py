from flask import Blueprint, jsonify

errors = Blueprint('error_pages',__name__)

@errors.app_errorhandler(404)
def error_404(error):
    return jsonify({"Message": "404 Not Found"}), 404

@errors.app_errorhandler(500)
def error_500(error):
    return jsonify({"Message": "500 Server Error"}), 500

#401 Unauthorized
#405 Method Not Allowed
#420 Enhance Your Calm
#429 Too Many Requests
