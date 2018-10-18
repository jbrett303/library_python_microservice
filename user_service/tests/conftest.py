"""setup fixtures for pytest"""
import pytest

from user_service import create_app, DB
from user_service.models import User, Rental

@pytest.fixture(scope='module')
def new_user():
    """fixture to test user class"""
    user = User('Ralph Realname', 'ralphr@legit.co')
    return user

@pytest.fixture(scope='module')
def new_rental():
    """fixture to test rental class"""
    rental = Rental(1, 2)
    return rental

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

    user1 = User('Bob Readerson', 'bobr@readingrainbow.com')
    user2 = User('Billy Bookhound', 'billyb@literacycorner.org')
    DB.session.add(user1)
    DB.session.add(user2)

    DB.session.commit()

    yield DB

    DB.drop_all()
