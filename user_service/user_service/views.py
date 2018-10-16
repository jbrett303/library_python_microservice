import requests
from flask import jsonify, Blueprint
from user_service import db
from user_service.models import Rental

user_routes = Blueprint('user_routes', __name__)

@user_routes.route('/health')
def health():
    return "user is so healthy"

@user_routes.route('/books')
def books():
    res = requests.get('http://libserv:5000/books')
    return res.content, res.status_code

@user_routes.route('/checkout/<int:book_id>/<int:user_id>', methods=['POST'])
def checkout(book_id, user_id):
    res = requests.post(f'http://libserv:5000/checkout/{book_id}')
    if res.status_code != requests.codes.ok:
        return res
    r = Rental(book_id, user_id)
    db.session.add(r)
    db.session.commit()
    return jsonify({
        'book id': book_id,
        'user_id': user_id,
        'status': 'deployed for learnin'
        }), 200

@user_routes.route('/return/<int:book_id>/<int:user_id>', methods=['POST'])
def re_uh_give_back(book_id, user_id):
    res = requests.post(f'http://libserv:5000/return/{book_id}')
    if res.status_code != requests.codes.ok:
        return res
    rental = Rental.query.filter((Rental.book_id == book_id) & (Rental.user_id == user_id)).first()
    if not rental:
        return "rental not found", 400
    db.session.delete(rental)
    db.session.commit()
    return jsonify({
        'book id': book_id,
        'user_id': user_id,
        'status': 'returned'
        }), 200

@user_routes.route('/rentalstatus')
def rentalstatus():
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
