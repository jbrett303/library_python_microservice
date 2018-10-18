"""unit tests"""

def test_new_book(new_book):
    """test new book init"""
    assert new_book.book_id is None
    assert new_book.title == 'The Booktastical Book'
    assert new_book.author == 'Author McAuthorson'
    assert new_book.in_stock is None
