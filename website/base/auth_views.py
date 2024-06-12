from flask import Blueprint , render_template , request , flash
from . import db
from .models import User

bp = Blueprint('auth',__name__,url_prefix='/auth') 

@bp.route('/login', methods=['GET','POST'])
def login():
    return render_template("login.html")


@bp.route('/logout')
def logout():
    return render_template("logout.html")

@bp.route('/sign-up', methods = ['GET','POST'])
def sign_up():
    if request.method == 'POST':
        user_name = request.form.get('userName')
        email = request.form.get('email')
        password1 = request.form.get('password')
        password2 = request.form.get('password2')


        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(user_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            pass
    return render_template("sign_up.html")