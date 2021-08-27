from flask import render_template
from app import app

@app.route("/")
def index():
    title = "Home"
    greeting = "Hello, World!"
    return render_template("index.html", title=title, greeting=greeting)
