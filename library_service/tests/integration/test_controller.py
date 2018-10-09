def test_health(test_client):
    res = test_client.get('/health')
    assert b"library is so healthy" in res.data

def test_books(test_client):
    res = test_client.get('/books')
    assert b"test book title 1" in res.data
    assert b"test book title 2" in res.data
    assert b"test book author 1" in res.data
    assert b"test book author 2" in res.data