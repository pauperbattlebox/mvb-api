from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_caching import Cache
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

db = SQLAlchemy()
migrate = Migrate()
cache = Cache(config = {'CACHE_TYPE': 'RedisCache',
                        'CACHE_REDIS_URL': environ.get('REDISTOGO_URL')})
limiter = Limiter(key_func=get_remote_address)
