import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

#local imports
from user_service.database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email


class Rental(Base):
    __tablename__ = 'rentals'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'))
    out = Column(DateTime, nullable=False, default=datetime.datetime.now())
    due = Column(DateTime, nullable=False, default=datetime.datetime.now() +
                 datetime.timedelta(days=7))

    def __init__(self, book_id, user_id):
        self.book_id = book_id
        self.user_id = user_id
