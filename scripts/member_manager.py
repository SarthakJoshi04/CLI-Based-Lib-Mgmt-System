import csv
import os

from scripts.member import Member

class MemberManager:
    MEMBERS_FILE_NAME = os.path.join("csv", "members.csv")
    MEMBERS_FILE_HEADERS = ["member_id", "name", "contact"]

    def __init__(self):
        self.__members = []
        self.load_members()

    def load_members(self):
        """
        Loads members from a CSV file into the member list.
        If the file does not exist, it creates a new file with the appropriate headers.
        """
        try:
            with open(self.MEMBERS_FILE_NAME, "r") as file:
                reader = csv.DictReader(file, fieldnames = self.MEMBERS_FILE_HEADERS)
                next(reader, None)
                for member in reader:
                    self.__members.append(
                        Member(member["name"], member["contact"], member["member_id"])
                    )
        except FileNotFoundError:
            with open(self.MEMBERS_FILE_NAME, "w") as file:
                writer = csv.DictWriter(file, fieldnames = self.MEMBERS_FILE_HEADERS)
                writer.writeheader()

    def list_members(self):
        """
        Lists all the members in the member list.
        """
        if not self.__members:
            print("\nNo members available.")
        for member in self.__members:
            print(member)

    def add_member(self, member):
        """
        Adds a member to the member list. If the member already exists, it ignores it. Also, it writes the member to the CSV file.
        Args:
            member (Member): The member object to be added.
        """
        for mem in self.__members:
            if mem.name == member.name and mem.contact == member.contact: # check for duplicate member
                print("\nMember already exists....\nIgnoring....")
                return
        
        self.__members.append(member)

        with open(self.MEMBERS_FILE_NAME, "a") as file:
            writer = csv.DictWriter(file, fieldnames = self.MEMBERS_FILE_HEADERS)
            writer.writerow(member.to_dict())
        
        print("\nMember added successfully....")

    def update_member(self, member):
        """
        Updates a member in the member list. If the member does not exist, it ignores it. Also, it updates the member in the CSV file.
        Args:
            member (Member): The member object to be updated.
        """
        for mem in self.__members:
            if mem.member_id == member.member_id:
                mem.name = member.name
                mem.contact = member.contact
                break
        else: # Else block will execute if the loop completes without a break
            print("\nMember does not exist....")
            return
            
        with open(self.MEMBERS_FILE_NAME, "w") as file:
            writer = csv.DictWriter(file, fieldnames = self.MEMBERS_FILE_HEADERS)
            writer.writeheader()
            for mem in self.__members:
                writer.writerow(mem.to_dict())
        
        print("\nMember updated successfully....")
    
    def remove_member(self, member_id):
        """
        Removes a member from the member list. If the member does not exist, it ignores it. Also, it updates the CSV file.
        Args:
            member_id (str): The member ID of the member to be removed.
        """
        for mem in self.__members:
            if mem.member_id == member_id:
                self.__members.remove(mem)
                break
        else: # Else block will execute if the loop completes without a break
            print("\nMember does not exist....")
            return
        
        with open(self.MEMBERS_FILE_NAME, "w") as file:
            writer = csv.DictWriter(file, fieldnames = self.MEMBERS_FILE_HEADERS)
            writer.writeheader()
            for mem in self.__members:
                writer.writerow(mem.to_dict())
        
        print("\nMember removed successfully....")

    def member_exists(self, member_id):
        """
        Checks if a member exists in the system.
        Args:
            member_id (str): The ID of the member to check.
        Returns:
            bool: True if the member exists, False otherwise.
        """
        return any(mem.member_id == member_id for mem in self.__members)

    def get_member_by_id(self, member_id):
        """
        Retrieves a member object by its ID.
        Args:
            book_id (str): The ID of the member to retrieve.
        Returns:
            Book: The member object if found, None otherwise.
        """
        for mem in self.__members:
            if mem.member_id == member_id:
                return mem
        return None
