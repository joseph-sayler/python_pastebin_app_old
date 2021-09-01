import os
from dotenv import load_dotenv
from dataclasses import dataclass

basedir = os.path.abspath(os.path.dirname("."))
load_dotenv(os.path.join(basedir, '.env'))

@dataclass
class Database_config:
    DATABASE = os.environ.get('DATABASE', None)
    DATABASE_TYPE = os.environ.get('DATABASE_TYPE', None)


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'very-special-key')

