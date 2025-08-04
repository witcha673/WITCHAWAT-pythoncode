
def contact_book():
    """
    Contact management system using dictionaries
    Each contact: {"name": str, "phone": str, "email": str, "category": str}
    """
    
    # Initialize empty contacts dictionary
    # Key: contact name (string), Value: contact info (dictionary)
    contacts = {
        "John Doe": {"phone": "123-456-7890", "email": "john@example.com", "category": "friend"},
        "Jane Smith": {"phone": "987-654-3210", "email": "jane@example.com", "category": "work"},
    }
    
    def add_contact():
        """Add a new contact to the address book"""
        print("\n=== Add New Contact ===")
        
        # Get contact information from user
        name = input("Enter contact name: ").strip()
        
        # TODO: Check if contact already exists
        # If exists, ask user if they want to update
        
        phone = input("Enter phone number: ").strip()
        email = input("Enter email address: ").strip()
        category = input("Enter category (family/friend/work/other): ").strip().lower()
        
        # TODO: Create contact dictionary and add to contacts
        contact_info = {
            # Fill in the contact information
        }
        
        # TODO: Add contact to the contacts dictionary
        
        
        print(f"Contact '{name}' added successfully!")
    
    def view_contact():
        """View details of a specific contact"""
        print("\n=== View Contact ===")
        
        if not contacts:
            print("No contacts found!")
            return
        
        name = input("Enter contact name to view: ").strip()
        
        # TODO: Check if contact exists and display information
        # Format the output nicely
        
        pass
    
    def search_contacts():
        """Search contacts by name, phone, or email"""
        print("\n=== Search Contacts ===")
        
        if not contacts:
            print("No contacts found!")
            return
        
        search_term = input("Enter search term (name/phone/email): ").strip().lower()
        
        # TODO: Search through all contacts
        # Check if search term appears in name, phone, or email
        # Display all matching contacts
        
        found_contacts = []
        
        # TODO: Implement search logic
        
        if found_contacts:
            print(f"\nFound {len(found_contacts)} contact(s):")
            # TODO: Display found contacts
        else:
            print("No contacts found matching your search.")
    
    def list_all_contacts():
        """Display all contacts in a formatted way"""
        print("\n=== All Contacts ===")
        
        if not contacts:
            print("No contacts found!")
            return
        
        print(f"{'Name':<20} {'Phone':<15} {'Email':<25} {'Category':<10}")
        print("-" * 70)
        
        # TODO: Implement listing logic
        
        pass
    
    def update_contact():
        """Update an existing contact"""
        print("\n=== Update Contact ===")
        
        if not contacts:
            print("No contacts found!")
            return
        
        name = input("Enter contact name to update: ").strip()
        
        # TODO: Check if contact exists
        # If exists, show current information
        # Ask what field to update
        # Update the contact information
        
        pass
    
    def delete_contact():
        """Delete a contact"""
        print("\n=== Delete Contact ===")
        
        if not contacts:
            print("No contacts found!")
            return
        
        name = input("Enter contact name to delete: ").strip()
        
        # TODO: Check if contact exists
        # Ask for confirmation
        # Delete the contact
        
        pass
    
    def contacts_by_category():
        """Group and display contacts by category"""
        print("\n=== Contacts by Category ===")
        
        if not contacts:
            print("No contacts found!")
            return
        
        # TODO: Group contacts by category
        # Use a dictionary where key=category, value=list of contacts
        # Display each category with its contacts
        
        categories = {}
        
        # TODO: Implement grouping logic
        
        pass
    
    def contact_statistics():
        """Show statistics about the contact book"""
        print("\n=== Contact Statistics ===")
        
        if not contacts:
            print("No contacts found!")
            return
        
        # TODO: Calculate and display:
        # - Total number of contacts
        # - Number of contacts per category
        # - Most common category
        # - Contacts with missing information (empty fields)
        
        total_contacts = len(contacts)
        print(f"Total contacts: {total_contacts}")
        
        # TODO: Implement statistics calculation
        
        pass
    
    # Main menu loop
    while True:
        print("\n" + "="*50)
        print("           CONTACT BOOK MANAGER")
        print("="*50)
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Search Contacts")
        print("4. List All Contacts")
        print("5. Update Contact")
        print("6. Delete Contact")
        print("7. Contacts by Category")
        print("8. Contact Statistics")
        print("9. Exit")
        print("-"*50)
        
        choice = input("Enter your choice (1-9): ").strip()
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contact()
        elif choice == "3":
            search_contacts()
        elif choice == "4":
            list_all_contacts()
        elif choice == "5":
            update_contact()
        elif choice == "6":
            delete_contact()
        elif choice == "7":
            contacts_by_category()
        elif choice == "8":
            contact_statistics()
        elif choice == "9":
            print("Thank you for using Contact Book Manager!")
            break
        else:
            print("Invalid choice! Please enter a number between 1-9.")

if __name__ == "__main__":
    print("Starting Contact Book Manager...")
    
    contact_book()