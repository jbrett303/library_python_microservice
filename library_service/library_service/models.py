"""app models"""
from library_service import DB

class Book(DB.Model):
    """book model"""
    __tablename__ = 'books'
    book_id = DB.Column(DB.Integer, primary_key=True)
    title = DB.Column(DB.String(100))
    author = DB.Column(DB.String(50))
    in_stock = DB.Column(DB.Boolean(), default=True)

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
