import os
from dotenv import load_dotenv
from dataclasses import dataclass


TOKEN_SIZE = 5

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


# @dataclass
# class Database_config:
#     DATABASE = os.environ.get('DATABASE', None)
#     DATABASE_TYPE = os.environ.get('DATABASE_TYPE', None)


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY', 'very-special-key')
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'paste_db.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
