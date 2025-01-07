from scripts.book import Book
from scripts.member import Member
from scripts.assignment import Assignment

from scripts.book_manager import BookManager
from scripts.member_manager import MemberManager
from scripts.assignment_manager import AssignmentManager

def main():
    print("<--- Welcome to the Library Management System --->")
    
    while(True):
        book_manager = BookManager()
        member_manager = MemberManager()
        assignment_manager = AssignmentManager()

        print("\nChoose an option:")
        print("1. List all Books")
        print("2. Add a Book")
        print("3. Remove a Book")
        print("4. Update a Book")

        print("\n5. List all Members")
        print("6. Add a Member")
        print("7. Remove a Member")
        print("8. Update a Member")

        print("\n9. List all Assignments")
        print("10. Assign a Book")
        print("11. Return a Book")
        print("12. Exit")

        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Invalid Input. Please try again")
            continue

        match choice:
            case 1:
                print("List of Books")
                book_manager.list_books()
                print("<------------------------------------------------->")
            case 2:
                print("Adding a Book...")
                title = input("Enter Title: ")
                author = input("Enter Author: ")
                quantity = int(input("Enter Quantity: "))
                book = Book(title, author, quantity)
                book_manager.add_book(book)
                print("<------------------------------------------------->")
            case 3:
                print("Removing a Book...")
                book_id = input("Enter Book ID: ")
                book_manager.delete_book1(book_id)
                print("<------------------------------------------------->")
            case 4:
                print("Updating a Book...")
                book_id = input("Enter Book ID: ")
                title = input("Enter Title: ")
                author = input("Enter Author: ")
                quantity = int(input("Enter Quantity: "))
                book = Book(title, author, quantity, book_id)
                book_manager.update_book(book)
                print("<------------------------------------------------->")
            case 5:
                print("List of Members")
                member_manager.list_members()
                print("<------------------------------------------------->")
            case 6:
                print("Adding a Member...")
                name = input("Enter Name: ")
                contact = input("Enter Contact: ")
                member = Member(name, contact)
                member_manager.add_member(member)
                print("<------------------------------------------------->")
            case 7:
                print("Removing a Member...")
                member_id = input("Enter Member ID: ")
                member_manager.remove_member(member_id)
                print("<------------------------------------------------->")
            case 8:
                print("Updating a Member...")
                member_id = input("Enter Member ID: ")
                name = input("Enter Name: ")
                contact = input("Enter Contact: ")
                member = Member(name, contact, member_id)
                member_manager.update_member(member)
                print("<------------------------------------------------->")
            case 9:
                print("List of Assignments")
                assignment_manager.list_assignments()
                print("<------------------------------------------------->")
            case 10:
                print("Assigning a Book...")
                member_id = input("Enter Member ID: ")
                book_id = input("Enter Book ID: ")

                if not member_manager.member_exists(member_id):
                    print("Member does not exist!")
                    break

                if not book_manager.book_exists(book_id):
                    print("Book does not exist!")
                    break

                assignment = Assignment(member_id, book_id)
                assignment_manager.assign_book(assignment)
                print("<------------------------------------------------->")
            case 11:
                print("Returning a Book...")
                assignment_id = input("Enter Assignment ID: ")
                assignment_manager.return_book(assignment_id)
                print("<------------------------------------------------->")
            case 12:
                print("Exiting the Library Management System....")
                break


if __name__ == "__main__":
    main()