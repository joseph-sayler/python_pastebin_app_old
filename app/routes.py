from secrets import token_urlsafe
from flask import Blueprint, render_template, request, redirect, abort
from app.models import Pastes

routes = Blueprint('routes', __name__)


@routes.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form.get("title").strip()
        paste_text = request.form.get("paste-text").strip()
        identifier = token_urlsafe(5)
        paste = Pastes(identifier=identifier,
                       paste_text=paste_text,
                       title=title)
        paste.save()
        return redirect(request.host_url + identifier)
    return render_template("index.html")


@routes.route("/<string:paste_id>/")
def render_paste(paste_id):
    try:
        paste = Pastes.get(Pastes.identifier == paste_id)
    except:
        abort(404)
    return render_template("results.html", paste=paste, date_format="MMM Do, YYYY [@] h:mm A")
