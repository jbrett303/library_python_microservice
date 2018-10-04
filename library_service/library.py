import json
import time
from flask import Flask
import controller

app = Flask(__name__)

@app.route('/health')
def health():
    return "library is so healthy"

@app.route('/books')
def books():
    return controller.get_books()

@app.route('/checkout/<int:book_id>', methods=['POST'])
def checkout(book_id):
    return controller.checkout_book(book_id)

@app.route('/return/<int:book_id>', methods=['POST'])
def re_uh_give_back(book_id):
    return controller.return_book(book_id)
