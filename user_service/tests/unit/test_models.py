
def test_new_user(new_user):
    """test new user init"""
    assert new_user.name == 'Ralph Realname'
    assert new_user.email == 'ralphr@legit.co'


def test_new_rental(new_rental):
    """test new rental init"""
    assert new_rental.book_id == 1
    assert new_rental.user_id == 2
    