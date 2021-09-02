import peewee
from datetime import datetime
from config import Database_config
from app.database import Database


class Pastes(peewee.Model):
    """table to hold user pastes"""
    identifier = peewee.TextField()
    title = peewee.TextField()
    paste_text = peewee.TextField()
    date = peewee.DateTimeField(default=datetime.utcnow())

    class Meta:
        db = Database(config=Database_config)
        database = db.database
