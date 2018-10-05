#library controllers


def get_books():
    return "books"

def checkout_book(book_id):
    return "checkout book {0}".format(book_id)

def return_book(book_id):
    return "return book {0}".format(book_id)
