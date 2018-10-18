"""app models"""
import datetime
from user_service import DB

class User(DB.Model):
    """User model"""
    __tablename__ = 'users'
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(50), unique=True)
    email = DB.Column(DB.String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email


class Rental(DB.Model):
    """Rental mmodel"""
    __tablename__ = 'rentals'
    id = DB.Column(DB.Integer, primary_key=True)
    book_id = DB.Column(DB.Integer)
    user_id = DB.Column(DB.Integer)
    out = DB.Column(DB.DateTime, nullable=False, default=datetime.datetime.now)
    due = DB.Column(DB.DateTime, nullable=False, default=datetime.datetime.now() +
                    datetime.timedelta(days=7))

    def __init__(self, book_id, user_id):
        self.book_id = book_id
        self.user_id = user_id
