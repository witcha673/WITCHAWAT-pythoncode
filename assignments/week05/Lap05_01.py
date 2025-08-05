# add_contact() 

# view_contact() 
# def view_contact(name, contacts):
#     # TODO: Implement view_contact function
#     pass

# search_contacts() 
# def search_contacts(query, contacts):
#     # TODO: Implement search_contacts function
#     pass

# list_all_contacts() 

# update_contact() 
# def update_contact(name, contacts):
#     # TODO: Implement update_contact function
#     pass

# delete_contact() – ลบผู้ติดต่อออกจากระบบ
# def delete_contact(name, contacts):
#     # TODO: Implement delete_contact function
#     pass

def add_contact():
    student = {}
    student["name"] = input("Enter name: ")
    student["phone"] = input("Enter phone number: ")
    student["email"] = input("Enter email: ")
    return student

def view_contact(name, contacts):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            return
    print("Contact not found.")

def search_contacts(query, contacts):
    found = False
    for contact in contacts:
        if (query.lower() in contact["name"].lower() or
            query in contact["phone"] or
            query.lower() in contact["email"].lower()):
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            found = True
    if not found:
        print("No contact matched your search.")

def list_all_contacts(contacts):
    if not contacts:
        print("No contacts yet.")
    else:
        print("=== รายชื่อทั้งหมด ===")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def update_contact(name, contacts):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("Updating contact...")
            contact["phone"] = input("New phone: ")
            contact["email"] = input("New email: ")
            print("Contact updated.")
            return
    print("Contact not found.")

def delete_contact(name, contacts):
    for i, contact in enumerate(contacts):
        if contact["name"].lower() == name.lower():
            confirm = input(f"Are you sure you want to delete {contact['name']}? (y/n): ").lower()
            if confirm == "y":
                contacts.pop(i)
                print("Contact deleted.")
            else:
                print("Cancelled.")
            return
    print("Contact not found.")
