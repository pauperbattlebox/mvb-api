from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

from .extensions import cache, db, limiter

current_version = "/api/v1/"


def create_app():
    app = Flask(__name__)

    # app.config.from_pyfile("config.py")
    app.config.from_object("application.config.ProdConfig")

    db.init_app(app)
    cache.init_app(app)
    limiter.init_app(app)

    from application import models

    with app.app_context():

        app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1)

        from .cards.routes import cards
        from .core.routes import core
        from .errors.errors import errors
        from .sets.routes import sets

        app.register_blueprint(core)
        app.register_blueprint(sets)
        app.register_blueprint(cards)
        app.register_blueprint(errors)

        return app
