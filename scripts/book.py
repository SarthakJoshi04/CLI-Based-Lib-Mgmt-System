import uuid

class Book:
    def __init__(self, title, author, quantity, book_id = None):       
        self.__title = title
        self.__author = author
        self.__quantity = int(quantity)
        self.__book_id = str(uuid.uuid4().int)[:5] if book_id is None else book_id

    def __str__(self):
        return f"Book -> Book ID = {self.__book_id} | Title: {self.__title} | Author: {self.__author} | Quantity: {self.__quantity}"
    
    def to_dict(self):
        return {
            "book_id": self.__book_id,
            "title": self.__title,
            "author": self.__author,
            "quantity": self.__quantity
        }
    
    # Getter methods for private attributes
    # These methods are used to access the private attributes of the class outside of the class as a read-only attribute.
    @property
    def book_id(self):
        return self.__book_id
    
    @property
    def title(self):
        return self.__title
    
    @property
    def author(self):
        return self.__author
    
    @property
    def quantity(self):
        return self.__quantity
    
    # Setter methods for private attributes
    # These methods are used to modify the private attributes of the class outside of the class.
    @title.setter
    def title(self, title):
        self.__title = title

    @author.setter
    def author(self, author):
        self.__author = author

    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity