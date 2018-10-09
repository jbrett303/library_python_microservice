import datetime

#local imports
from library_service import db

class Book(db.Model):
    __tablename__ = 'books'
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(50))
    in_stock = db.Column(db.Boolean(), default=True)

    def __init__(self, title, author):
        self.title = title
        self.author = author


    def to_json(self):
        return {
            'book_id': self.book_id,
            'title': self.title,
            'author': self.author,
            'in_stock': self.in_stock
        }
