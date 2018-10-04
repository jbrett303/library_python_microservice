#user controllers
import requests


def get_books():
    res = requests.get('http://libserv:5000/books')
    print(res.status_code)
    return str(res.status_code)


def checkout_book(book_id):
    #hit the put on library to flag out
    #check for error
    #if good then hit user db: user has book etc
    return "checkout book {0}".format(book_id)


def return_book(book_id):
    #hit the put on library to flag in
    #check for error
    #if good then hit user db: user has returned book etc
    return "return book {0}".format(book_id)



## future functions

# def who has the book
# def search for book by author
# def search for book by etc...
