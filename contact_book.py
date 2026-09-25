contacts = {}

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")

    contacts[name] = {
        "phone": phone,
        "email": email
    }

    print("Saved Successfully.")


def view_contacts():
    if not contacts:
        print("No contacts found.")
        return

    print(f"{'NAME':<20}{'PHONE':<15}{'EMAIL'}")

    for name, details in contacts.items():
        print(f"{name:<20}{details['phone']:<15}{details['email']}")


def search_contact():
    search = input("Enter name to search: ").lower()

    found = False

    for name, details in contacts.items():
        if search in name.lower():
            print(f"Name: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            found = True

    if not found:
        print("Contact not found.")


def delete_contact():
    name = input("Enter name to delete: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")



def main():
    while True:
        print("\n--- CONTACT BOOK ---")
        print("1. Add")
        print("2. View all")
        print("3. Search")
        print("4. Delete")
        print("5. Quit")

        choice = input("Choose: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")




main()
