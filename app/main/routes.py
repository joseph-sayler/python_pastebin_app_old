from app import db
from secrets import token_urlsafe
from flask import render_template, request, redirect, abort
from app.models import Pastes
from app.main import bp
from config import TOKEN_SIZE


@bp.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form.get("title").strip()
        paste_text = request.form.get("paste-text").strip()
        identifier = token_urlsafe(TOKEN_SIZE)
        paste = Pastes(identifier=identifier,
                       paste_text=paste_text, title=title)
        db.session.add(paste)
        db.session.commit()
        return redirect(request.host_url + identifier)
    return render_template("index.html")


@bp.route("/<string:paste_id>/")
def render_paste(paste_id):
    try:
        paste = Pastes.query.get(paste_id)
    except:
        abort(404)
    return render_template("results.html", paste=paste, date_format="MMM Do, YYYY [@] h:mm A")
