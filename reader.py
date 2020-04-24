import pprint
import PyPDF4

class Reader:
    """A class to simulate an e-book reading system.
    
    attr:
    
    purchased: list of purchased books
    
    BOOKS: a class level list containing the books in the system."""
    BOOKS =  {
        'book' : ["Data Structures and Algorithms in Python.pdf",
                "Python cookbook, 2nd Edition.pdf",
                "Learning Python, 5th Edition.pdf",
                "Dive into Python 3.pdf",
                "Learning Python.4th.Edition.Sep.2009.pdf",
                "Python Algorithms.pdf"],
    'price': [20,20,20,20,20,20]
    }

    def __init__(self):
        self._purchased = list()

    def buy_book(self,book,price):
        """checks if book is in store and appends to the list of purchased books"""
        if book in Reader.BOOKS['book'] and price in Reader.BOOKS['price']:
            self._purchased.append(book)
        else:
            return "sorry we don't have this book, come back later"

    @property
    def purchased(self):
        return self._purchased

    def read(self,book):
        if book in self._purchased:
            with open(book,"rb") as book:
                reader = PyPDF4.PdfFileReader(book)
                for i in range(reader.getNumPages()):
                    page = reader.getPage(i)
                    text = page.extractText()
                    pprint.pprint(text)
                    print("\n")
        else:
            return "book not in your purchased books. are you sure you have this book?"

    def __str__(self):
        return "An E-book Reader"