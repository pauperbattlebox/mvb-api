from flask import Flask

from .extensions import db, migrate, cache

current_version = '/api/v1/'

def create_app():
    app = Flask(__name__)

    app.config.from_pyfile("config.py")

    db.init_app(app)
    migrate.init_app(app, db)
    cache.init_app(app)

    from application import models


    with app.app_context():

        from .core.routes import core
        from .sets.routes import sets
        from .cards.routes import cards
        from .errors.errors import errors

        app.register_blueprint(core)
        app.register_blueprint(sets)
        app.register_blueprint(cards)
        app.register_blueprint(errors)

        return app
