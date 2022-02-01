from flask import Blueprint, jsonify

errors = Blueprint('error_pages',__name__)

@errors.app_errorhandler(400)
def error_400(error):
    return jsonify({"Message": error.description}), 400

@errors.app_errorhandler(404)
def error_404(error):
    return jsonify({"Message": "404 Not Found"}), 404

@errors.app_errorhandler(429)
def error_429(error):
    return jsonify({"Message": "429 Enhance Your Calm. Please add 300ms between each request."}), 429

@errors.app_errorhandler(500)
def error_500(error):
    return jsonify({"Message": "500 Server Error"}), 500
