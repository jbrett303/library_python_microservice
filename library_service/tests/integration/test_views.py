
def test_health(test_client):
    res = test_client.get('/health')
    assert b"library is so healthy" in res.data

def test_books(test_client, init_database):
    res = test_client.get('/books')
    assert b"test book title 1" in res.data
    assert b"test book title 2" in res.data
    assert b"test book author 1" in res.data
    assert b"test book author 2" in res.data
    
def test_add_book(test_client, init_database):
    #happy path
    res = test_client.post('/add/bestbook/bobwriterson')
    assert b"book added sucessfully" in res.data
    assert res.status_code == 200
    res = test_client.get('books')
    books = res.get_json()
    for book in books:
        if book['book_id'] == 3:
            assert book['title'] == 'bestbook'
            assert book['author'] == 'bobwriterson'

def test_checkout_book(test_client, init_database):
    #happy path
    res = test_client.post('/checkout/1')
    assert b"Book 1, checked out succesfully!" in res.data
    assert res.status_code == 200
    res = test_client.get('books')
    books = res.get_json()
    for book in books:
        if book['book_id'] == 1:
            assert book['in_stock'] == False
        else:
            assert book['in_stock'] == True
    #exception path
    res = test_client.post('/checkout/1')
    assert b'book is already checked out' in res.data
    assert res.status_code == 400

def test_return_book(test_client, init_database):
    test_client.post('/checkout/1')
    res = test_client.post('/return/1')
    assert b"Book 1, checked back in succesfully!" in res.data
    assert res.status_code == 200
    res = test_client.get('books')
    books = res.get_json()
    for book in books:
        if book['book_id'] == 1:
            assert book['in_stock'] == True
        else:
            assert book['in_stock'] == True
    #exception path
    res = test_client.post('/return/1')
    assert b'book is already checked in' in res.data
    assert res.status_code == 400
