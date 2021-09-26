from flask import Flask
from .extensions import db, migrate


def create_app(config_file='config.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)

    db.init_app(app)
    migrate.init_app(app, db)

    from application import models


    with app.app_context():

        from .core.routes import core
        from .set.routes import sets
        from .cards.routes import cards

        app.register_blueprint(core)
        app.register_blueprint(sets)
        app.register_blueprint(cards)

        return app
