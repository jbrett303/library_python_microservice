import datetime

#local imports
from user_service import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email


class Rental(db.Model):
    __tablename__ = 'rentals'
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    out = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    due = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now() +
                    datetime.timedelta(days=7))

    def __init__(self, book_id, user_id):
        self.book_id = book_id
        self.user_id = user_id
