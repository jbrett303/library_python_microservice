from library_service import controller
from flask import Blueprint

library_routes = Blueprint('library_routes', __name__)

@library_routes.route('/health')
def health():
    return "library is so healthy"

@library_routes.route('/books')
def books():
    return controller.get_books()

@library_routes.route('/checkout/<int:book_id>', methods=['POST'])
def checkout(book_id):
    return controller.checkout_book(book_id)

@library_routes.route('/return/<int:book_id>', methods=['POST'])
def re_uh_give_back(book_id):
    return controller.return_book(book_id)

@library_routes.route('/add/<string:title>/<string:author>', methods=['POST'])
def add(title, author):
    return controller.add_book(title, author)
