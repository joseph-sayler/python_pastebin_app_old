import click, peewee, os
from app import models


def register(app):
    @app.cli.command("create-pastes-table")
    def create_table():
        """create the pastes_db.db file and add the Pastes table. does nothing if table already exists
        """
        try:
            models.Pastes.create_table()
        except peewee.OperationalError:
            print("Pastes table already exists in database")
