import pytest

from library_service import create_app, db
from library_service.models import Book

@pytest.fixture(scope='module')
def new_book():
    book = Book('The Booktastical Book', 'Author McAuthorson')
    return book

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
 
    # Insert book data
    book1 = Book('test book title 1','test book author 1')
    book2 = Book('test book title 2','test book author 2')
    db.session.add(book1)
    db.session.add(book2)
 
    # Commit the changes
    db.session.commit()
 
    yield db  # this is where the testing happens!
 
    db.drop_all()