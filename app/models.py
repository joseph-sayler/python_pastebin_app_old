import peewee
from datetime import datetime
from config import Database_config
from app.database import Database


db = Database(config=Database_config)


class BaseModel(peewee.Model):
    """A base model that uses a database object to determine which database to instantiate"""
    class Meta:
        database = db.database


# db_wrapper.Model superclass allows app factory pattern to
# be used to create the database; now the database info is
# part of the flask configuration instead of stated here
class Pastes(BaseModel):
    """table to hold user pastes"""
    identifier = peewee.TextField()
    title = peewee.TextField()
    paste_text = peewee.TextField()
    date = peewee.DateTimeField(default=datetime.utcnow())
