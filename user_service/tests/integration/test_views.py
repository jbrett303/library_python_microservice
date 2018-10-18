"""tests for view.py"""
from flask import current_app

class MockBook:
    """defines a test book item to enable modification at test level"""
    def __init__(self, book_id, title, author, in_stock):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.in_stock = in_stock


    def to_json(self):
        """returns a json representaion of the mock book object"""
        return {
            'book_id': self.book_id,
            'title': self.title,
            'author': self.author,
            'in_stock': self.in_stock
        }

BOOK1 = MockBook(1, 'test book title 1', 'test book author 1', True)
BOOK2 = MockBook(2, 'test book title 2', 'test book author 2', True)
BOOKS = [BOOK1, BOOK2]

def json_books():
    """returns a books json array from the constants above"""
    return [book.to_json() for book in BOOKS]


def test_health(test_client):
    """tests the health endpoint"""
    res = test_client.get('/health')
    assert b"user is so healthy" in res.data

def test_books(test_client, requests_mock):
    """tests the books endpoint, mocks the library service call"""
    requests_mock.register_uri('GET',
                               current_app.config['BOOKS_URI'],
                               json=json_books(),
                               status_code=200)

    res = test_client.get('/books')
    assert b"test book title 1" in res.data
    assert b"test book title 2" in res.data
    assert b"test book author 1" in res.data
    assert b"test book author 2" in res.data


def test_checkout_book(test_client, init_database, requests_mock):
    """tests the checkout endpoint, mocks the library service call"""
    print(current_app.config['CHECKOUT_URI'].format(1))
    #setup mock for library service call
    requests_mock.register_uri('PUT', 
                               current_app.config['CHECKOUT_URI'].format(1),
                               text='''Book 1, checked out succesfully!
                               test book title 1 is due back in 7 days''',
                               status_code=200)
    #happy path
    res = test_client.post('/books/1/1/checkout')
    assert b"deployed for learnin" in res.data
    assert res.status_code == 200
    #exception path
    #setup mock for library service call
    requests_mock.register_uri('PUT',
                               current_app.config['CHECKOUT_URI'].format(1),
                               text="book is already checked out",
                               status_code=400)
    res = test_client.post('/books/1/1/checkout')
    assert b'book is already checked out' in res.data
    assert res.status_code == 400
