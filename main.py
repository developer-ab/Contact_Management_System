# Importing the required libraries
import json           # For reading/writing contact data in JSON format
import os             # For file handling operations like checking file existence
import re             # For validating email and phone formats using regex

# File where contact data will be stored
CONTACT_FILE = 'contacts.txt'

# Contact class defines a structure to store individual contact details
class Contact:

    # Constructor to initialize contact details
    def __init__(self, name, phone, email, tags):
        self.name = name
        self.phone = phone
        self.email = email
        self.tags = tags

    # Converts the contact object to a dictionary format for easy storage in JSON
    def to_dict(self):
        return {
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'tags': self.tags
        }

    # Static method to create a Contact object from a dictionary
    @staticmethod
    def from_dict(data):
        return Contact(data['name'], data['phone'], data['email'], data['tags'])


# ContactManager class manages the operations on all contacts
class ContactManager:

    # Constructor initializes the contacts list by loading existing data
    def __init__(self):
        self.contacts = self.load_contacts()

    # Loads contact data from the file into a list of Contact objects
    def load_contacts(self):
        contacts = []
        if os.path.exists(CONTACT_FILE):  # Check if file exists before reading
            with open(CONTACT_FILE, 'r') as f:
                for line in f:
                    data = json.loads(line)             # Convert JSON string to dictionary
                    contact = Contact.from_dict(data)   # Convert dictionary to Contact object
                    contacts.append(contact)            # Add contact to list
        return contacts

    # Saves all current contacts back into the file in JSON format
    def save_contacts(self):
        with open(CONTACT_FILE, 'w') as f:
            for contact in self.contacts:
                f.write(json.dumps(contact.to_dict()) + "\n")  # Convert each contact to JSON string and save

    # Validates international phone number (e.g., +91xxxxxxxxxx) using regex
    def is_valid_phone(self, phone):
        return re.fullmatch(r'^\+\d{1,4}\d{10}$', phone) is not None

    # Validates email using regex pattern
    def is_valid_email(self, email):
        return re.fullmatch(r'^[\w\.-]+@[\w\.-]+\.\w{2,}$', email) is not None

    # Adds a new contact after validation and duplication check
    def add_contact(self, contact):
        if not self.is_valid_phone(contact.phone):
            raise ValueError("Invalid phone number. Must include country code followed by 10 digits.")
        if not self.is_valid_email(contact.email):
            raise ValueError("Invalid email format.")

        # Check for duplicate phone number
        for c in self.contacts:
            if c.phone == contact.phone:
                raise ValueError("Contact with this phone number already exists.")

        self.contacts.append(contact)  # Add the new contact
        self.save_contacts()           # Save to file

    # Searches contacts using a regex pattern in name, phone, or tags
    def search_contacts(self, pattern):
        try:
            regex = re.compile(pattern, re.IGNORECASE)  # Compile search pattern
        except re.error:
            raise ValueError("Invalid regular expression.")
        
        # Match name, phone, or any tag
        results = [c for c in self.contacts if regex.search(c.name) or regex.search(c.phone) or any(regex.search(tag) for tag in c.tags)]
        if not results:
            raise LookupError("No contact found.")
        return results

    # Returns all contacts, optionally sorted by name
    def get_all_contacts(self, sort_by_name=True):
        return sorted(self.contacts, key=lambda c: c.name.lower()) if sort_by_name else self.contacts

    # Deletes contact(s) by matching name (case insensitive)
    def delete_contact(self, name):
        original_count = len(self.contacts)
        self.contacts = [c for c in self.contacts if c.name.lower() != name.lower()]
        if len(self.contacts) == original_count:
            raise LookupError("Contact not found.")
        self.save_contacts()

    # Edits a contact by finding it using old phone number
    def edit_contact(self, old_phone, new_contact):
        # Validate new contact data
        if not self.is_valid_phone(new_contact.phone):
            raise ValueError("Invalid phone number. Must include country code followed by 10 digits.")
        if not self.is_valid_email(new_contact.email):
            raise ValueError("Invalid email format.")

        for i, contact in enumerate(self.contacts):
            if contact.phone == old_phone:
                # Check if the new phone number already exists in another contact
                if new_contact.phone != old_phone:
                    for c in self.contacts:
                        if c.phone == new_contact.phone:
                            raise ValueError("Another contact with this phone number already exists.")
                self.contacts[i] = new_contact  # Replace the old contact with new data
                self.save_contacts()
                return
        raise LookupError("Contact with given phone number not found.")

    # Deletes contact by phone number
    def delete_contact_by_phone(self, phone):
        original_count = len(self.contacts)
        self.contacts = [c for c in self.contacts if c.phone != phone]
        if len(self.contacts) == original_count:
            raise LookupError("Contact not found.")
        self.save_contacts()

