from datetime import datetime
from config import TOKEN_SIZE
from config import Database_config
from flask_sqlalchemy import SQLAlchemy
from app.database import Fauna_DB


if Database_config.DATABASE_TYPE == "FAUNA":
    db = Fauna_DB()

    class Fauna_Pastes:
        """table to hold user pastes"""

        def __init__(self, identifier=None, title=None, paste_text=None, date=None):
            self.identifier = identifier
            self.title = title
            self.paste_text = paste_text
            self.date = date if date else datetime.utcnow()

        def _from_dict(self, data):
            for key, value in data.items():
                setattr(self, key, value)

        def __repr__(self):
            return f'<Paste {self.identifier}>'
else:  # == "SQLITE"
    db = SQLAlchemy()

    class SQL_Pastes(db.Model):
        """table to hold user pastes"""

        identifier = db.Column(db.String(TOKEN_SIZE),
                               nullable=False, unique=True, primary_key=True)
        title = db.Column(db.Text, nullable=False)
        paste_text = db.Column(db.Text, nullable=False)
        date = db.Column(db.DateTime, nullable=False,
                         default=datetime.utcnow())

        def __repr__(self):
            return f'<Paste {self.identifier}>'
