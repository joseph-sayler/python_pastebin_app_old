import os
from dotenv import load_dotenv


TOKEN_SIZE = 5

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Database_config:
    DATABASE = os.environ.get('DATABASE', None)
    DATABASE_TYPE = os.environ.get('DATABASE_TYPE', None)

class Fauna_config:
    FAUNA_SECRET_KEY = os.environ.get("FAUNA_SECRET_KEY", None)
    FAUNA_DOMAIN = os.environ.get("FAUNA_DOMAIN", None)
    FAUNA_COLLECTION = os.environ.get("FAUNA_COLLECTION", None)
    FAUNA_INDEX = os.environ.get("FAUNA_INDEX", None)


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'very-special-key')
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'paste_db.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
