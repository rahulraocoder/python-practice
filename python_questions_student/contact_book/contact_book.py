"""
Contact Book Problem

Objective:
Implement a simple contact book that can:
- Add contacts (name, phone, email)
- Search by any field (name, phone, email)
- Prevent duplicate entries
- Save/load contacts to JSON file

Example Contact:
{
    "name": "John Doe",
    "phone": "1234567890", 
    "email": "john@example.com"
}
"""

class ContactBook:
    def __init__(self):
        """Initialize empty contact book"""
        self.contacts = []

    def add_contact(self, name, phone, email):
        """
        Add a new contact if not already existing
        
        Args:
            name (str): Contact name
            phone (str): Phone number
            email (str): Email address
            
        Returns:
            bool: True if added, False if duplicate
        """
        # TODO: Implement contact addition
        pass

    def search(self, query):
        """
        Search contacts by any field
        
        Args:
            query (str): Search term
            
        Returns:
            list: Matching contacts
        """
        # TODO: Implement search
        pass

    def save_to_file(self, filename):
        """Save contacts to JSON file"""
        # TODO: Implement JSON save
        pass

    def load_from_file(self, filename):
        """Load contacts from JSON file"""
        # TODO: Implement JSON load
        pass
