from flask import Blueprint

bp = Blueprint('auth',__name__,url_prefix='/auth') 

@bp.route('/login')
def login():
    return "<h1>login</h1>"

@bp.route('/logout')
def logout():
    return "<h1>logout</h1>"

@bp.route('/sign-up')
def sign_up():
    return "<h1>sign up</h1>"