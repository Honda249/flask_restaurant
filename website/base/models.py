from . import db
from flask_login import UserMixin


# Database Models

# User model
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    user_name = db.Column(db.String(150))
    reservations = db.relationship('Reservation')


# Reservation model
class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    table_id = db.Column(db.Integer, db.ForeignKey('table.id'))

# Table Model 
class Table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10000))
    description = db.Column(db.String(10000))
    reservations = db.relationship('Reservation')

