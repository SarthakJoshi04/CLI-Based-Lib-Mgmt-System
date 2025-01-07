import csv
import os

from scripts.assignment import Assignment
from scripts.book_manager import BookManager
from scripts.member_manager import MemberManager

class AssignmentManager:
    ASSIGNMENT_FILE_NAME = os.path.join("csv", "assignments.csv")
    ASSIGNMENT_FILE_HEADERS = ["assignment_id", "member_id", "book_id", "issue_date", "due_date", "returned"]

    book_manager = BookManager()
    member_manager = MemberManager()

    def __init__(self):
        self.__assignments = []
        self.load_assignments()

    def load_assignments(self):
        """
        Loads assignments from a CSV file into the assignments list.
        If the file does not exist, it creates a new file with the appropriate headers.
        """
        try:
            with open(self.ASSIGNMENT_FILE_NAME, "r") as file:
                reader = csv.DictReader(file, fieldnames=self.ASSIGNMENT_FILE_HEADERS)
                next(reader, None)
                for assignment in reader:
                    self.__assignments.append(
                        Assignment(
                            assignment["member_id"],
                            assignment["book_id"],
                            assignment["issue_date"],
                            assignment["due_date"],
                            assignment["returned"] == "True", # Convert the string to a boolean
                            assignment["assignment_id"]
                        )
                    )
        except FileNotFoundError:
            with open(self.ASSIGNMENT_FILE_NAME, "w") as file:
                writer = csv.DictWriter(file, fieldnames=self.ASSIGNMENT_FILE_HEADERS)
                writer.writeheader()


    def list_assignments(self):
        """
        Lists all assignments in the assignments list.
        """
        if not self.__assignments:
            print("\nNo assignments available.")
        for assignment in self.__assignments:
            print(assignment)

    def assign_book(self, assignment):
        """
        Assigns a book to a member.
        Reduces the book's quantity and adds the assignment to the list and CSV file.
        """
        book = self.book_manager.get_book_by_id(assignment.book_id)
        if book is None:
            print("\nBook not found!")
            return

        if book.quantity <= 0:
            print("\nBook is out of stock!")
            return

        # Reduce book quantity
        book.quantity -= 1
        self.book_manager.update_book(book)

        # Add assignment
        self.__assignments.append(assignment)
        with open(self.ASSIGNMENT_FILE_NAME, "a") as file:
            writer = csv.DictWriter(file, fieldnames=self.ASSIGNMENT_FILE_HEADERS)
            writer.writerow(assignment.to_dict())

        print("\nBook assigned successfully!")

    def return_book(self, assignment_id):
        """
        Marks a book as returned.
        Increases the book's quantity and updates the assignment in the CSV file.
        """
        for assignment in self.__assignments:
            if assignment.assignment_id == assignment_id:
                if assignment.returned == "Returned":
                    print("\nBook is already marked as returned.")
                    return

                # Mark as returned
                assignment.returned = True

                # Increase book quantity
                book = self.book_manager.get_book_by_id(assignment.book_id)
                if book:
                    book.quantity += 1
                    self.book_manager.update_book(book)

                # Update CSV file
                with open(self.ASSIGNMENT_FILE_NAME, "w") as file:
                    writer = csv.DictWriter(file, fieldnames=self.ASSIGNMENT_FILE_HEADERS)
                    writer.writeheader()
                    for assign in self.__assignments:
                        writer.writerow(assign.to_dict())

                print("\nBook returned successfully!")
                return

        print(f"\nError: Assignment with ID {assignment_id} not found.")