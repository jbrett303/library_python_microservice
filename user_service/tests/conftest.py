import pytest
from requests_mock import Adapter
from requests import Session
from flask import jsonify

from user_service import create_app, db
from user_service.models import User, Rental

@pytest.fixture(scope='module')
def new_user():
    user = User('Ralph Realname', 'ralphr@legit.co')
    return user

@pytest.fixture(scope='module')
def new_rental():
    rental = Rental(1, 2)
    return rental

@pytest.fixture(scope='module')
def test_client():
    app = create_app('test.cfg')
    testing_client = app.test_client()
    
    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()
 
    yield testing_client  # this is where the testing happens!
 
    ctx.pop()

@pytest.fixture(scope='module')
def init_database():
    # Create the database and the database table
    db.create_all()
 
    # Insert user data
    user1 = User('Bob Readerson', 'bobr@readingrainbow.com')
    user2 = User('Billy Bookhound', 'billyb@literacycorner.org')
    db.session.add(user1)
    db.session.add(user2)
 
    # Commit the changes
    db.session.commit()
 
    yield db  # this is where the testing happens!
 
    db.drop_all()

@pytest.fixture
def mock_library_service():

    bookRes = jsonify(
            {'book_id': '1',
            'title': 'test book title 1',
            'author': 'test book author 1',
            'in_stock': 'true'
            })

    adapter = Adapter()
    session = Session()

    adapter.register_uri('GET', 'http://libserv:5000/books', json=bookRes, status_code=200)

    session.mount('http', adapter)
    
