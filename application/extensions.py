from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_caching import Cache

from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))

db = SQLAlchemy()
migrate = Migrate()
cache = Cache(config = {'CACHE_TYPE': 'RedisCache',
                        'CACHE_REDIS_URL': environ.get('REDIS_URL')})
                        # 'CACHE_REDIS_HOST': environ.get('CACHE_REDIS_HOST'),
                        # 'CACHE_REDIS_PORT': environ.get('CACHE_REDIS_PORT'),
                        # 'CACHE_REDIS_PASSWORD': environ.get('CACHE_REDIS_PASSWORD'),
                        # })
