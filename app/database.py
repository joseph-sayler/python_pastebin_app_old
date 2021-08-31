from playhouse.flask_utils import FlaskDB


class Database:
    """class to handle database selection"""

    def __init__(self, app=None):
        self._app = app
        self.flaskDB = FlaskDB()
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self._app = app
        if 'DATABASE_TYPE' in app.config:
            if app.config['DATABASE_TYPE'] == "ORM":
                self.flaskDB.init_app(app)
            elif app.config['DATABASE_TYPE'] == "FAUNA":
                pass
            else:
                pass
