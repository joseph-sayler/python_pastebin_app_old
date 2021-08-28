from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment

moment = Moment()
bootstrap = Bootstrap()

def create_app():
    # "Application Factory" pattern as described in the Flask docs:
    # http://flask.pocoo.org/docs/patterns/appfactories/

    app = Flask(__name__)

    moment.init_app(app)
    bootstrap.init_app(app)
    
    from app.routes import routes
    app.register_blueprint(routes)

    return app
