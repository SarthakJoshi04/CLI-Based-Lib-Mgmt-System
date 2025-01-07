import uuid
from datetime import datetime, timedelta

class Assignment:
    def __init__(self, member_id, book_id, issue_date = None, due_date = None, returned = False, assignment_id = None):
        self.__member_id = member_id
        self.__book_id = book_id
        self.__issue_date = datetime.now().strftime("%d/%m/%Y") if issue_date is None else issue_date

        # Set due_date to 20 days after issue_date if not provided
        if due_date is None:
            # Parse the issue date (a string in "dd/mm/yyyy" format) into a datetime object
            issue_datetime = datetime.strptime(self.__issue_date, "%d/%m/%Y")
            # Add 20 days to the issue date to calculate the due date and convert it back to a string in "dd/mm/yyyy" format
            self.__due_date = (issue_datetime + timedelta(days = 20)).strftime("%d/%m/%Y")
        else:
            self.__due_date = due_date

        self.__returned = returned
        self.__assignment_id = str(uuid.uuid4().int)[:5] if assignment_id is None else assignment_id
    
    def __str__(self):
        return f"Assignment -> Assignment ID: {self.__assignment_id} | Member ID: {self.__member_id} | Book ID: {self.__book_id} | Issue Date: {self.__issue_date} | Due Date: {self.__due_date} | Returned: {'Yes' if self.__returned else 'No'}"
    
    def to_dict(self):
        return {
            "assignment_id": self.__assignment_id,
            "member_id": self.__member_id,
            "book_id": self.__book_id,
            "issue_date": self.__issue_date,
            "due_date": self.__due_date,
            "returned": self.__returned
        }

    # Getter methods for private attributes
    # These methods are used to access the private attributes of the class outside of the class as a read-only attribute.
    @property
    def assignment_id(self):
        return self.__assignment_id

    @property
    def member_id(self):
        return self.__member_id

    @property
    def book_id(self):
        return self.__book_id

    @property
    def issue_date(self):
        return self.__issue_date

    @property
    def due_date(self):
        return self.__due_date

    @property
    def returned(self):
        return "Returned" if self.__returned else "Not Returned"

    # Setter methods for private attributes
    # These methods are used to modify the private attributes of the class outside of the class.
    @returned.setter
    def returned(self, returned):
        self.__returned = returned