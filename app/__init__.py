import click, peewee, os
from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

# place at bottom to avoid circular imports
from app import routes, models

@app.cli.command("create-pastes-table")
def create_user():
    """create the pastes_db.db file and add the Pastes table. does nothing if table already exists
    """
    try:
        models.Pastes.create_table()
    except peewee.OperationalError:
        print("Pastes table already exists in database")
