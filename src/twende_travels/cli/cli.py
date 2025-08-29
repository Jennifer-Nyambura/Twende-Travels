from twende_travels.db.database import get_session
from twende_travels.models.models import Customer, Booking, Account

# -----------------------------
# Authentication
# -----------------------------

def register():
    print("\n--- Register ---")
    username = input("Enter username: ")
    password = input("Enter password: ")

    session = get_session()
    existing = session.query(Account).filter_by(username=username).first()

    if existing:
        print("Username already exists. Try another one.")
    else:
        new_account = Account(username=username, password=password)
        session.add(new_account)
        session.commit()
        print("Account created successfully! You can now log in.")

    session.close()
    input("\nPress Enter to continue...")

def login():
    print("\n--- Login ---")
    username = input("Username: ")
    password = input("Password: ")

    session = get_session()
    account = session.query(Account).filter_by(username=username, password=password).first()
    session.close()

    if account:
        print(f"Welcome back, {account.username}!")
        return True
    else:
        print("Invalid username or password.")
        return False

# -----------------------------
# Customers & Bookings
# -----------------------------

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
        for c in customers:
            print(f" - {c.id}: {c.name} ({c.email})")
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
    print(f"Booking to '{destination}' on {date} created for {customer.name}!")

    session.close()
    input("\nPress Enter to return to menu...")

def add_customer_with_booking():
    print("\n--- Add Customer with Booking ---")
    name = input("Enter customer name: ")
    email = input("Enter customer email: ")
    destination = input("Enter booking destination: ")
    date = input("Enter booking date (YYYY-MM-DD): ")

    session = get_session()

    # Create customer
    new_customer = Customer(name=name, email=email)
    session.add(new_customer)
    session.flush()  # ensure new_customer.id is ready

    # Create booking
    new_booking = Booking(destination=destination, date=date, customer=new_customer)
    session.add(new_booking)
    session.commit()

    print(f"✔️ Customer '{new_customer.name}' and booking to '{destination}' added successfully!")

    session.close()
    input("\nPress Enter to return to menu...")

def list_bookings():
    session = get_session()
    bookings = session.query(Booking).all()
    session.close()

    if bookings:
        print(f"\nBooking List ({len(bookings)} total):")
        for b in bookings:
            print(f" - {b.id}: {b.customer.name} booked {b.destination} on {b.date}")
    else:
        print("\nNo bookings found.")
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

# -----------------------------
# Main Menu
# -----------------------------

def main_menu():
    logged_in = False
    while not logged_in:
        print("\n--- Twende Travels ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            register()
        elif choice == "2":
            logged_in = login()
        elif choice == "3":
            print("Goodbye!")
            return
        else:
            print("Invalid choice. Try again.")

    while True:
        print("\n--- Main Menu ---")
        print("1. Add Customer")
        print("2. List Customers")
        print("3. Update Customer")
        print("4. Delete Customer")
        print("5. Add Booking")
        print("6. List Bookings")
        print("7. Delete Booking")
        print("8. Add Customer with Booking")
        print("9. Logout")
        print("10. Exit")

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
            add_customer_with_booking()
        elif choice == "9":
            print("Logging out...")
            return main_menu()
        elif choice == "10":
            print("Goodbye! Thanks for using Twende Travels.")
            break
        else:
            print("Invalid choice, try again.")
