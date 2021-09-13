from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from config import Config, Database_config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.database import Fauna_DB


if Database_config.DATABASE_TYPE == "FAUNA":
    db = Fauna_DB
else:  # == "SQLITE"
    db = SQLAlchemy()
migrate = Migrate()
moment = Moment()
bootstrap = Bootstrap()


def create_app(config_class=Config):
    # "Application Factory" pattern as described in the Flask docs:
    # http://flask.pocoo.org/docs/patterns/appfactories/

    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    
    if Database_config.DATABASE_TYPE == "SQLITE":
    migrate.init_app(app, db)

    moment.init_app(app)
    bootstrap.init_app(app)

    from app.main import bp as app_main
    app.register_blueprint(app_main)

    return app
