import csv
import os

from scripts.book import Book

class BookManager:
    BOOKS_FILE_NAME = os.path.join("csv", "books.csv")
    BOOKS_FILE_HEADERS = ["book_id", "title", "author", "quantity"]

    def __init__(self):
        self.__books = []
        self.load_books()

    def load_books(self):
        """
        Loads books from a CSV file into the book list.
        If the file does not exist, it creates a new file with the appropriate headers.
        """
        try:
            with open(self.BOOKS_FILE_NAME, "r") as file:
                reader = csv.DictReader(file, fieldnames = self.BOOKS_FILE_HEADERS)
                next(reader, None)
                for book in reader:
                    self.__books.append(
                        Book(book["title"], book["author"], book["quantity"], book["book_id"])
                    )
        except FileNotFoundError:
            with open(self.BOOKS_FILE_NAME, "w") as file:
                writer = csv.DictWriter(file, fieldnames = self.BOOKS_FILE_HEADERS)
                writer.writeheader()

    def list_books(self):
        """
        Lists all the books in the book list.
        """
        if not self.__books:
            print("\nNo books available.")
        for book in self.__books:
            print(book)
    
    def add_book(self, book):
        """
        Adds a book to the book list. If the book already exists, it ignores it. Also, it writes the book to the CSV file.
        Args:
            book (Book): The book object to be added.
        """
        for bks in self.__books:
            if bks.title == book.title and bks.author == book.author: # check for duplicate book
                print("\nBook already exists....\nIgnoring....")
                return
   
        self.__books.append(book)

        with open(self.BOOKS_FILE_NAME, "a") as file:
            writer = csv.DictWriter(file, fieldnames = self.BOOKS_FILE_HEADERS)
            writer.writerow(book.to_dict())

        print("\nBook added successfully....")
    
    def update_book(self,book):
        """
        Updates a book in the book list. If the book does not exist, it ignores it. Also, it updates the CSV file.
        Args:
            book (Book): The book object to be updated.
        """
        for bks in self.__books: 
            if bks.book_id == book.book_id: # check for the corresponding book to update
                bks.title = book.title
                bks.author = book.author
                bks.quantity = book.quantity
                break
        else: # Else block will execute if the loop completes without a break
            print("\nBook does not exist....")
            return
    
        with open(self.BOOKS_FILE_NAME, "w") as file:
            writer = csv.DictWriter(file, fieldnames = self.BOOKS_FILE_HEADERS)
            writer.writeheader()
            for bks in self.__books:
                writer.writerow(bks.to_dict())

        print("\nBook updated successfully....")

    def delete_book(self, book_id):
        """
        Deletes a book from the book list. If the book does not exist, it ignores it. Also, it updates the CSV file.
        Args:
            book_id (str): The book ID of the book to be deleted.
        """
        for book in self.__books:
            if book.book_id == book_id:
                self.__books.remove(book)
                break
        else: # Else block will execute if the loop completes without a break
            print("\nBook does not exist....")
            return

        with open(self.BOOKS_FILE_NAME, "w") as file:
            writer = csv.DictWriter(file, fieldnames = self.BOOKS_FILE_HEADERS)
            writer.writeheader()
            for bks in self.__books:
                writer.writerow(bks.to_dict())

        print("\nBook deleted successfully....")


    def book_exists(self, book_id):
        """
        Checks if a book exists in the system.
        Args:
            book_id (str): The ID of the book to check.
        Returns:
            bool: True if the book exists, False otherwise.
        """
        return any(book.book_id == book_id for book in self.__books)

    def get_book_by_id(self, book_id):
        """
        Retrieves a book object by its ID.
        Args:
            book_id (str): The ID of the book to retrieve.
        Returns:
            Book: The book object if found, None otherwise.
        """
        for book in self.__books:
            if book.book_id == book_id:
                return book
        return None