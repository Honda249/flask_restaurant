from flask import Blueprint , render_template

bp = Blueprint('reservation',__name__,url_prefix='/reservations')

@bp.route('/')
def create_reservation():
    return render_template("reservation.html")

@bp.route('/delete')
def delete_reservation():
    return render_template("delete-reservation.html")

