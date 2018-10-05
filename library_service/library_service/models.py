import datetime

from sqlalchemy import Column, Integer, String, Boolean
from library_service.database import Base

class Books(Base):
    __tablename__ = 'books'
    book_id = Column(Integer, primary_key=True)
    title = Column(String(100))
    author = Column(String(50))
    status = Column(Boolean())

    def __init__(self, book_id, title, author, status):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = status
