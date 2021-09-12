from app import db
from datetime import datetime
from config import TOKEN_SIZE


class Pastes(db.Model):
    """table to hold user pastes"""
    identifier = db.Column(db.String(TOKEN_SIZE),
                           nullable=False, unique=True, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    paste_text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    def __repr__(self):
        return f'<Paste {self.identifier}>'
