# UTechLinks System
# CNS1001 


# DATA STORAGE (Dictionaries)

users = {}
services = {
    "Food": [{"name": "Lunch Special", "price": 800, "available": True}],
    "Transport": [{"name": "Taxi Discount", "price": 500, "available": True}],
    "Printing": [{"name": "Print 10 pages", "price": 200, "available": True}]
}


# FUNCTIONS


def register():
    print("\n--- Registration ---")
    name = input("Enter name: ")
    stud_id = input("Enter student ID: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    # Validate input
    if stud_id in users:
        print("Error: User already exists.")
    else:
        users[student_id] = {
            "name": name,
            "email": email,
            "password": password
        }
        print("Registration successful!")


def login():
    print("\n--- Login ---")
    stud_id = input("Enter student ID: ")
    password = input("Enter password: ")

    # Authenticate user
    if stud_id in users and users[student_id]["password"] == password:
        print("Login successful!")
        return stud_id
    else:
        print("Access denied.")
        return None


def view_services():
    print("\n--- Available Services ---")
    for category, items in services.items():
        print(f"\n{category}:")
        for i, item in enumerate(items):
            status = "Available" if item["available"] else "Unavailable"
            print(f"{i + 1}. {item['name']} - ${item['price']} ({status})")


def request_service():
    view_services()
    category = input("\nEnter category: ")

    if category in services:
        try:
            choice = int(input("Select item number: ")) - 1
            item = services[category][choice]

            # Check availability
            if item["available"]:
                print(f"Request confirmed for {item['name']}")
                item["available"] = False  # Update inventory
            else:
                print("Item not available.")
        except:
            print("Invalid selection.")
    else:
        print("Invalid category.")


def admin_menu():
    print("\n--- Admin Menu ---")
    print("1. Add Service")
    print("2. Remove Service")
    print("3. View Reports")

    choice = input("Choose option: ")

    if choice == "1":
        category = input("Enter category: ")
        name = input("Enter service name: ")
        price = float(input("Enter price: "))

        new_item = {"name": name, "price": price, "available": True}

        if category in services:
            services[category].append(new_item)
        else:
            services[category] = [new_item]

        print("Service added successfully.")

    elif choice == "2":
        category = input("Enter category: ")
        if category in services:
            view_services()
            try:
                index = int(input("Enter item number to remove: ")) - 1
                services[category].pop(index)
                print("Service removed.")
            except:
                print("Invalid selection.")
        else:
            print("Category not found.")

    elif choice == "3":
        generate_reports()

    else:
        print("Invalid option.")


def generate_reports():
    print("\n--- Reports ---")
    print(f"Total Users: {len(users)}")

    total_services = sum(len(items) for items in services.values())
    print(f"Total Services: {total_services}")

    available = sum(item["available"] for items in services.values() for item in items)
    print(f"Available Services: {available}")



# MAIN PROGRAM

def main():
    while True:
        print("\n=== UTechLinks ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Select option: ")

        if choice == "1":
            register()

        elif choice == "2":
            user = login()
            if user:
                while True:
                    print("\n--- User Menu ---")
                    print("1. View Services")
                    print("2. Request Service")
                    print("3. Admin Menu")
                    print("4. Logout")

                    option = input("Choose option: ")

                    if option == "1":
                        view_services()
                    elif option == "2":
                        request_service()
                    elif option == "3":
                        admin_menu()
                    elif option == "4":
                        break
                    else:
                        print("Invalid option.")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


# Run program
main()