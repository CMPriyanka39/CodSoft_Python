class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = {
            'name': name,
            'phone': phone,
            'email': email,
            'address': address
        }
        self.contacts.append(contact)
        print(f"Contact {name} added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("Contact List:")
            for contact in self.contacts:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}")

    def search_contact(self, keyword):
        results=''
        for contact in self.contacts:
            if keyword.lower() in contact['name'].lower() or keyword in contact['phone']:
                results+=f"Name: {contact['name']}\n Phone: {contact['phone']}\n Address: {contact['address']}\nEmail: {contact['email']} \n\n"
        return results

    def update_contact(self, name, new_phone, new_email, new_address):
        for contact in self.contacts:
            if contact['name'] == name:
                contact['phone'] = new_phone
                contact['email'] = new_email
                contact['address'] = new_address
                print(f"Contact {name} updated successfully.")
                return
        print(f"Contact {name} not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact['name'] == name:
                self.contacts.remove(contact)
                print(f"Contact {name} deleted successfully.")
                return
        print(f"Contact {name} not found.")

def validate_name(name):
    if name.isalpha():  # Check if the name contains only non-digit characters
        return True
    else:
        print("Invalid name. Please enter a valid name without digits.")
        return False

def validate_address(address):
    if address.isalpha():  # Check if the address contains only non-digit characters
        return True
    else:
        print("Invalid address. Please enter a valid address without digits.")
        return False

def validate_phone(phone):
    if phone.isdigit() and len(phone) == 10:  # Check if the phone is a 10-digit number
        return True
    else:
        print("Invalid phone number. Please enter a 10-digit number.")
        return False

def validate_email(email):
    # Basic email format check
    if '@' in email and '.' in email:
        return True
    else:
        print("Invalid email address. Please enter a valid email.")
        return False

contact_book = ContactBook()
while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = int(input("Enter your choice (1-6): "))
    match choice:
        case 1:
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            if (
            validate_name(name)
            and validate_phone(phone)
            and validate_email(email)
            and validate_address(address)
        ):
                contact_book.add_contact(name, phone, email, address)
                
        case 2:
            contact_book.view_contacts()

        case 3:
            keyword = input("Enter name or phone number to search: ")
            results = contact_book.search_contact(keyword)
            if results:
                print("Search Results:")
                print(results)
            else:
                print("No matching contacts found.")

        case 4:
            name = input("Enter name of contact to update: ")
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            if (
            validate_name(name)
            and validate_phone(new_phone)
            and validate_email(new_email)
            and validate_address(new_address)
        ):
                contact_book.update_contact(name, new_phone, new_email, new_address)

        case 5:
            name = input("Enter name of contact to delete: ")
            contact_book.delete_contact(name)

        case 6:
            print("Exiting Contact Book. Goodbye!")
            break

        case _:
            print("Invalid choice. Please enter a number between 1 and 6.")


