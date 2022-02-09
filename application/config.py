from os import environ, path

from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

SECRET_KEY = environ.get('SECRET_KEY')
SQLALCHEMY_TRACK_MODIFICATIONS=False
SQLALCHEMY_DATABASE_URI = environ.get('SQLALCHEMY_DATABASE_URI')
RATELIMIT_STORAGE_URI = environ.get('REDISTOGO_URL')
RATELIMIT_STRATEGY = 'moving-window'
JSON_SORT_KEYS = False
