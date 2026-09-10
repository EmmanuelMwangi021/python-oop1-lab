#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self._size = None
        self.size = size
        self.price = price

    @property  #defines a property for the size attribute.
    def size(self):
        return self._size

    @size.setter    #defines a setter for the size property that checks if the value is one of the allowed sizes.
    def size(self, value):
        if value not in ["small", "medium", "large"]:
            print("size must be 'small', 'medium', or 'large'")
        else:
            self._size = value

    
    def tip(self, amount=1):  #defines a method to simulate tipping the barista.
        self.price += amount 
        print("This coffee is great, here's a tip!")


coffee1 = Coffee("large", 50)
coffee1.tip()
