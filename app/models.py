import peewee
import pytz
from datetime import datetime

db = peewee.SqliteDatabase("paste_db.db")


class BaseModel(peewee.Model):
    class Meta:
        database = db


class Pastes(BaseModel):
    """
    table to hold user pastes
    """
    identifier = peewee.TextField()
    title = peewee.TextField()
    paste_text = peewee.TextField()
    date = peewee.DateTimeField(default=datetime.now(pytz.UTC))
