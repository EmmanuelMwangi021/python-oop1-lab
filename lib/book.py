#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = None
        self.page_count = page_count

        @property #it defines a property for the page_count(self)
        def page_count(self):
            return self._page_count

        @page_count.setter  # it defines a setter for the page_count property that checks if the value is an integer.
        def page_count(self, value):
            if not isinstance(value, int):
                print("page_count must be an integer")
            else:
                self._page_count = value

    def turn_page(self):   #it defines the method to simulate turning a page.
        print("Flipping the page...wow, you read fast!") 
    
#book1 = Book("The Great Gatsby", 160)   
#book1.turn_page()    