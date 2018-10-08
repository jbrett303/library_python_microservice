#user controllers
import requests
from flask import jsonify
from user_service import db
from user_service.models import Rental


def get_books():
    res = requests.get('http://libserv:5000/books')
    return res


def checkout_book(book_id, user_id):
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


def return_book(book_id, user_id):
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



## future functions

# def who has the book
# def search for book by author
# def search for book by etc...
