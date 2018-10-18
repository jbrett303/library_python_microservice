"""views"""
from flask import Blueprint, jsonify, request
from library_service import DB
from library_service.models import Book

LIBRARY_ROUTES = Blueprint('library_routes', __name__)

@LIBRARY_ROUTES.route('/health')
def health():
    """"health endpoint"""
    return "library is so healthy"

@LIBRARY_ROUTES.route('/books')
def get_books():
    """books endpoint returns all books in db"""
    books = Book.query.all()
    json_books = []
    for book in books:
        json_books.append(book.to_json())
    return jsonify(json_books), 200

@LIBRARY_ROUTES.route('/books/<int:book_id>/checkout', methods=['PUT'])
def checkout(book_id):
    """checkout endpoint flags book as out of stock or returns an error"""
    book = Book.query.filter(Book.book_id == book_id).first()
    if not book:
        return "book ID not found", 400
    if  not book.in_stock:
        return "book is already checked out", 400
    book.in_stock = False
    DB.session.add(book)
    DB.session.commit()
    return f"Book {book_id}, checked out succesfully!  {book.title} is due back in 7 days", 200

@LIBRARY_ROUTES.route('/books/<int:book_id>/return', methods=['PUT'])
def re_uh_give_back(book_id):
    """return endpoint, flags book as in stock or returns an error"""
    book = Book.query.filter(Book.book_id == book_id).first()
    if not book:
        return "book ID not found", 400
    if book.in_stock:
        return "book is already checked in", 400
    book.in_stock = True
    DB.session.add(book)
    DB.session.commit()
    return f"Book {book_id}, checked back in succesfully!", 200

@LIBRARY_ROUTES.route('/books/add', methods=['POST'])
def add():
    """adds a book to the system"""
    b = Book(request.form['title'], request.form['author'])
    DB.session.add(b)
    DB.session.commit()
    return jsonify({
        'book title': b.title,
        'author': b.author,
        'status': 'book added sucessfully'
        }), 200
