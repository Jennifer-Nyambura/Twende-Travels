from twende_travels.db.database import get_session
from twende_travels.models.models import Customer, Booking, Account

# Global variable to track logged-in user
current_user = None

def auth_menu():
    while True:
        print("\n--- Authentication ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            if login():
                main_menu()  # enter main system only if login success
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    session = get_session()
    existing = session.query(Account).filter_by(username=username).first()

    if existing:
        print("⚠️ Username already exists, try again.")
    else:
        new_account = Account(username=username, password=password)
        session.add(new_account)
        session.commit()
        print(f"✔️ Account created for {username}!")
    session.close()

def login():
    global current_user
    username = input("Enter username: ")
    password = input("Enter password: ")

    session = get_session()
    account = session.query(Account).filter_by(username=username, password=password).first()
    session.close()

    if account:
        current_user = account
        print(f"✔️ Welcome back, {username}!")
        return True
    else:
        print("❌ Invalid username or password.")
        return False

def main_menu():
    while True:
        print("\n Welcome to Twende Travels!")

        print("\n--- Customers ---")
        print("1. Add Customer")
        print("2. List Customers")
        print("3. Update Customer")
        print("4. Delete Customer")

        print("\n--- Bookings ---")
        print("5. Add Booking")
        print("6. List Bookings")
        print("7. Delete Booking")

        print("\n--- Exit ---")
        print("8. Logout")

        choice = input("\nEnter choice: ")

        if choice == "1":
            add_customer()
        elif choice == "2":
            list_customers()
        elif choice == "3":
            update_customer()
        elif choice == "4":
            delete_customer()
        elif choice == "5":
            add_booking()
        elif choice == "6":
            list_bookings()
        elif choice == "7":
            delete_booking()
        elif choice == "8":
            print("Logging out...")
            break
        else:
            print("Invalid choice, try again.")

def add_customer():
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")

    session = get_session()
    new_customer = Customer(name=name, email=email)
    session.add(new_customer)
    session.commit()
    session.close()

    print(f"Customer '{name}' added successfully!")
    input("\nPress Enter to return to menu...")

def list_customers():
    session = get_session()
    customers = session.query(Customer).all()
    session.close()

    if customers:
        print(f"\nCustomer List ({len(customers)} total):")
        # Example list usage
        names = [c.name for c in customers]
        print("Customer names (list):", names)

        for c in customers:
            # Example dict usage
            customer_dict = {"id": c.id, "name": c.name, "email": c.email}
            print(customer_dict)
    else:
        print("\nNo customers found.")
    input("\nPress Enter to return to menu...")

def update_customer():
    list_customers()
    try:
        customer_id = int(input("\nEnter the ID of the customer to update: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    session = get_session()
    customer = session.query(Customer).get(customer_id)

    if customer:
        print(f"Editing customer: {customer.name} ({customer.email})")
        new_name = input("Enter new name (leave blank to keep current): ")
        new_email = input("Enter new email (leave blank to keep current): ")

        if new_name.strip():
            customer.name = new_name
        if new_email.strip():
            customer.email = new_email

        session.commit()
        print(f"Customer '{customer.id}' updated successfully!")
    else:
        print(" No customer found with that ID.")

    session.close()
    input("\nPress Enter to return to menu...")

def delete_customer():
    list_customers()
    try:
        customer_id = int(input("\nEnter the ID of the customer to delete: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    session = get_session()
    customer = session.query(Customer).get(customer_id)

    if customer:
        session.delete(customer)
        session.commit()
        print(f"Customer '{customer.name}' deleted successfully!")
    else:
        print("No customer found with that ID.")

    session.close()
    input("\nPress Enter to return to menu...")

def add_booking():
    list_customers()
    try:
        customer_id = int(input("\nEnter the ID of the customer making the booking: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    session = get_session()
    customer = session.query(Customer).get(customer_id)

    if not customer:
        print("No customer found with that ID.")
        session.close()
        return

    destination = input("Enter booking destination: ")
    date = input("Enter booking date (YYYY-MM-DD): ")

    new_booking = Booking(destination=destination, date=date, customer=customer)
    session.add(new_booking)
    session.commit()

    # Example dict
    booking_dict = {"id": new_booking.id, "destination": new_booking.destination, "date": new_booking.date, "customer_id": new_booking.customer_id}
    print("Booking as dict:", booking_dict)

    session.close()
    print(f"Booking to '{destination}' on {date} created for {customer.name}!")
    input("\nPress Enter to return to menu...")

def list_bookings():
    session = get_session()
    bookings = session.query(Booking).all()
    session.close()

    if bookings:
        print(f"\n Booking List ({len(bookings)} total):")
        # Example tuple usage
        booking_tuples = [(b.id, b.customer.name, b.destination, b.date) for b in bookings]
        print("Booking tuples:", booking_tuples)

        for b in bookings:
            print(f" - {b.id}: {b.customer.name} booked {b.destination} on {b.date}")
    else:
        print("\n No bookings found.")
    input("\nPress Enter to return to menu...")

def delete_booking():
    list_bookings()
    try:
        booking_id = int(input("\nEnter the ID of the booking to delete: "))
    except ValueError:
        print("Invalid ID. Please enter a number.")
        return

    session = get_session()
    booking = session.query(Booking).get(booking_id)

    if booking:
        session.delete(booking)
        session.commit()
        print(f"Booking to '{booking.destination}' for {booking.customer.name} deleted successfully!")
    else:
        print("No booking found with that ID.")

    session.close()
    input("\nPress Enter to return to menu...")
