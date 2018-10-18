"""setup fixtures for pytest"""
import pytest

from library_service import create_app, DB
from library_service.models import Book

@pytest.fixture(scope='module')
def new_book():
    """fixture to test book class"""
    book = Book('The Booktastical Book', 'Author McAuthorson')
    return book

@pytest.fixture(scope='module')
def test_client():
    """test client for testing"""
    app = create_app('test.cfg')
    testing_client = app.test_client()

    ctx = app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()

@pytest.fixture(scope='module')
def init_database():
    """setup and teardown db for testing"""
    DB.create_all()

    book1 = Book('test book title 1', 'test book author 1')
    book2 = Book('test book title 2', 'test book author 2')
    DB.session.add(book1)
    DB.session.add(book2)

    DB.session.commit()

    yield DB

    DB.drop_all()
