from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from playhouse.flask_utils import FlaskDB


moment = Moment()
bootstrap = Bootstrap()
db_wrapper = FlaskDB()


def create_app():
    # "Application Factory" pattern as described in the Flask docs:
    # http://flask.pocoo.org/docs/patterns/appfactories/

    app = Flask(__name__)
    app.config['DATABASE'] = 'sqlite:///paste_db.db'

    moment.init_app(app)
    bootstrap.init_app(app)
    db_wrapper.init_app(app)

    from app.main import bp as app_main
    app.register_blueprint(app_main)

    return app
