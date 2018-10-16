from library_service import db
from library_service.models import Book
from flask import Blueprint, jsonify

library_routes = Blueprint('library_routes', __name__)

@library_routes.route('/health')
def health():
    return "library is so healthy"

@library_routes.route('/books')
def books():
    books = Book.query.all()
    json_books = []
    for book in books:
        json_books.append(book.to_json())
    return jsonify(json_books), 200

@library_routes.route('/checkout/<int:book_id>', methods=['POST'])
def checkout(book_id):
    book = Book.query.filter(Book.book_id == book_id).first()
    if not book:
        return "book ID not found", 400
    if  not book.in_stock:
        return "book is already checked out", 400
    book.in_stock = False
    db.session.add(book)
    db.session.commit()
    return f"Book {book_id}, checked out succesfully!  {book.title} is due back in 7 days", 200

@library_routes.route('/return/<int:book_id>', methods=['POST'])
def re_uh_give_back(book_id):
    book = Book.query.filter(Book.book_id == book_id).first()
    if not book:
        return "book ID not found", 400
    if book.in_stock:
        return "book is already checked in", 400
    book.in_stock = True
    db.session.add(book)
    db.session.commit()
    return f"Book {book_id}, checked back in succesfully!", 200

@library_routes.route('/add/<string:title>/<string:author>', methods=['POST'])
def add(title, author):
    b = Book(title, author)
    db.session.add(b)
    db.session.commit()
    return jsonify({
        'book title': title,
        'author': author,
        'status': 'book added sucessfully'
        }), 200
