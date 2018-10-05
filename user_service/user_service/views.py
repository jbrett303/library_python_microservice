from user_service import app
from user_service import controller

@app.route('/health')
def health():
    return "user is so healthy"

@app.route('/books')
def books():
    return controller.get_books()

@app.route('/checkout/<int:book_id>/<int:user_id>', methods=['POST'])
def checkout(book_id, user_id):
    return controller.checkout_book(book_id, user_id)

@app.route('/return/<int:book_id>/<int:user_id>', methods=['POST'])
def re_uh_give_back(book_id, user_id):
    return controller.return_book(book_id, user_id)

@app.route('/rentalstatus')
def rentalstatus():
    return controller.rentalstatus()
