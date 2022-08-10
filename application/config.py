from os import environ, path

from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


class Config:

    FLASK_ENV = "production"
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):

    SQLALCHEMY_DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")
    RATELIMIT_STORAGE_URI = environ.get("OPENREDIS_URL")
    RATELIMIT_STRATEGY = "moving-window"
    JSON_SORT_KEYS = False


class TestConfig(Config):
    RATELIMIT_ENABLED = False
    RATELIMIT_STORAGE_URI = "memory://"
