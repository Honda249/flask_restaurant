from flask import Blueprint , render_template

bp = Blueprint('reservation',__name__,url_prefix='')

@bp.route('/')
def home():
    return render_template("home.html")
    