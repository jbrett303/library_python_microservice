import json
import requests
from flask import jsonify

class test_book:

    def __init__(self, book_id, title, author, in_stock):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.in_stock = in_stock


    def to_json(self):
        return {
            'book_id': self.book_id,
            'title': self.title,
            'author': self.author,
            'in_stock': self.in_stock
        }

book1 = test_book(1,'test book title 1', 'test book author 1', True)
book2 = test_book(2,'test book title 2', 'test book author 2', True)
books = [book1, book2]

def json_books():
    return [book.to_json() for book in books]


def test_health(test_client):
    res = test_client.get('/health')
    assert b"user is so healthy" in res.data

def test_books(test_client, requests_mock):
    
    requests_mock.register_uri('GET', 'http://libserv:5000/books', json=json_books(), status_code=200)

    res = test_client.get('/books')
    assert b"test book title 1" in res.data
    assert b"test book title 2" in res.data
    assert b"test book author 1" in res.data
    assert b"test book author 2" in res.data


def test_checkout_book(test_client, init_database, requests_mock):
    #setup mock for library service call
    requests_mock.register_uri('POST', 'http://libserv:5000/checkout/1', text="Book 1, checked out succesfully!  test book title 1 is due back in 7 days", status_code=200)
    #happy path
    res = test_client.post('/checkout/1/1')
    assert b"deployed for learnin" in res.data
    assert res.status_code == 200
    #exception path
    #setup mock for library service call
    requests_mock.register_uri('POST', 'http://libserv:5000/checkout/1', text="book is already checked out", status_code=400)
    res = test_client.post('/checkout/1/1')
    assert b'book is already checked out' in res.data
    assert res.status_code == 400

