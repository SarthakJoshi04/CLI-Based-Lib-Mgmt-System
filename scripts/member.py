import uuid

class Member:
    def __init__(self, name, contact, member_id = None):
        self.__name = name
        self.__contact = contact
        self.__member_id = str(uuid.uuid4().int)[:5] if member_id is None else member_id

    def __str__(self):
        return f"Member -> Member ID: {self.__member_id} | Name: {self.__name} | Contact: {self.__contact}"
    
    def to_dict(self):
        return {
            "member_id": self.__member_id,
            "name": self.__name,
            "contact": self.__contact
        }
    
    # Getter methods for private attributes
    # These methods are used to access the private attributes of the class outside of the class as a read-only attribute.
    @property
    def member_id(self):
        return self.__member_id
    
    @property
    def name(self):
        return self.__name
    
    @property
    def contact(self):
        return self.__contact
    
    # Setter methods for private attributes
    # These methods are used to modify the private attributes of the class outside of the class.
    @name.setter 
    def name(self, name):
        self.__name = name

    @contact.setter
    def contact(self, contact):
        self.__contact = contact