


def test_new_book(new_book):
    assert new_book.book_id == None
    assert new_book.title == 'The Booktastical Book'
    assert new_book.author == 'Author McAuthorson'
    assert new_book.in_stock == None

