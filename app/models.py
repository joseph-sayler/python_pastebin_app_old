import peewee
from datetime import datetime
from app import db_wrapper

# db_wrapper.Model superclass allows app factory pattern to
# be used to create the database; now the database info is
# part of the flask configuration instead of stated here
class Pastes(db_wrapper.Model):
    """
    table to hold user pastes
    """
    identifier = peewee.TextField()
    title = peewee.TextField()
    paste_text = peewee.TextField()
    date = peewee.DateTimeField(default=datetime.utcnow())
