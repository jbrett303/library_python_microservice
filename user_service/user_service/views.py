"""views"""
import requests
from flask import jsonify, Blueprint, current_app
from user_service import DB
from user_service.models import Rental

USER_ROUTES = Blueprint('user_routes', __name__)

@USER_ROUTES.route('/health')
def health():
    """"health endpoint"""
    return "user is so healthy"

@USER_ROUTES.route('/books')
def books():
    """books endpoint, returns response from library service /books"""
    print(current_app.config['BOOKS_URI'])
    res = requests.get(current_app.config['BOOKS_URI'])
    return res.content, res.status_code

@USER_ROUTES.route('/books/<int:book_id>/<int:user_id>/checkout', methods=['POST'])
def checkout(book_id, user_id):
    """checkout endpoint, adds rental item to track user rental
    and communicates rental status to library service"""
    res = requests.put(current_app.config['CHECKOUT_URI'].format(book_id))
    if res.status_code != requests.codes.ok:
        return res.content, res.status_code
    r = Rental(book_id, user_id)
    DB.session.add(r)
    DB.session.commit()
    return jsonify({
        'book id': book_id,
        'user_id': user_id,
        'status': 'deployed for learnin'
        }), 200

@USER_ROUTES.route('/books/<int:book_id>/<int:user_id>/return', methods=['PUT'])
def re_uh_give_back(book_id, user_id):
    """return endpoint, deletes rental item and communicates rental status to library service"""
    res = requests.put(current_app.config['RETURN_URI'].format(book_id))
    if res.status_code != requests.codes.ok:
        return res
    rental = Rental.query.filter((Rental.book_id == book_id) & (Rental.user_id == user_id)).first()
    if not rental:
        return "rental not found", 400
    DB.session.delete(rental)
    DB.session.commit()
    return jsonify({
        'book id': book_id,
        'user_id': user_id,
        'status': 'returned'
        }), 200

@USER_ROUTES.route('/books/rentalstatus')
def rentalstatus():
    """rental status enpoint returns all the rentals in the system"""
    rentals = Rental.query.all()
    stats = []
    for rental in rentals:
        stats.append({
            'rental_id': rental.id,
            'book_id': rental.book_id,
            'user_id': rental.user_id,
            'checked_out': rental.out,
            'due_back': rental.due
        })
    return jsonify(stats), 200
