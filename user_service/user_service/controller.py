#user controllers
import requests
from flask import jsonify


def get_books():
    res = requests.get('http://libserv:5000/books')
    print(res.status_code)
    return str(res.status_code)


def checkout_book(book_id, user_id):
    #hit the put on library to flag out
    #check for error
    from user_service.database import db_session
    from user_service.models import Rental
    r = Rental(book_id, user_id)
    db_session.add(r)
    db_session.commit()
    return jsonify({
        'book id': book_id,
        'user_id': user_id,
        'status': 'deployed for learnin'
        }), 200


def return_book(book_id, user_id):
    from user_service.models import Rental
    rental = Rental.query.filter((Rental.book_id == book_id) & (Rental.user_id == user_id))
    if not rental:
        return "rental not found", 400
    #hit the put on library to flag in
    #check for error
    from user_service.database import db_session
    db_session.delete(rental)
    db_session.commit()
    return jsonify({
        'book id': book_id,
        'user_id': user_id,
        'status': 'returned'
        }), 200


def rentalstatus():
    from user_service.models import Rental
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
