from flask import Blueprint , render_template

bp = Blueprint('views',__name__,url_prefix='/views')

@bp.route('/')
def home():
    return render_template("home.html")
    