from flask import Blueprint , render_template

bp = Blueprint('auth',__name__,url_prefix='/auth') 

@bp.route('/login')
def login():
    return render_template("login.html")

@bp.route('/logout')
def logout():
    return render_template("logout.html")

@bp.route('/sign-up')
def sign_up():
    return render_template("sign-up.html")