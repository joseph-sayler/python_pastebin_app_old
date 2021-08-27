from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

# place at bottom to avoid circular imports
from app import routes
