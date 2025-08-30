from twende_travels.db.database import get_session
from twende_travels.models.models import Customer, Booking, Account
from tabulate import tabulate  # pip install tabulate

# ---------------- AUTH ----------------
def register_account():
    session = get_session()
    username = input("Choose a username: ").strip()
    password = input("Choose a password: ").strip()

    existing = session.query(Account).filter_by(username=username).first()
    if existing:
        print("⚠️ Username already exists. Try another.")
    else:
        account = Account(username=username, password=password)  # plain text password
        session.add(account)
        session.commit()
        print(f"✅ Account created for '{username}'")
    session.close()

def login_account():
    session = get_session()
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    account = session.query(Account).filter_by(username=username, password=password).first()
    if account:
        print(f"✅ Welcome back, {username}!")
        session.close()
        return True
    else:
        print("❌ Invalid username or password.")
        session.close()
        return False

def auth_menu():
    while True:
        print("\n--- Authentication ---")
        print("1. Register")
        print("2. Login")
        print("0. Exit")

        choice = input("Enter choice: ").strip()
        if choice == "1":
            register_account()
        elif choice == "2":
            if login_account():
                return True
        elif choice == "0":
            exit()
        else:
            print("❌ Invalid choice.")

# ---------------- MAIN MENU ----------------
def main_menu():
    while True:
        print("\n✨ Welcome to Twende Travels ✨")
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
        print("0. Exit")

        choice = input("\nEnter choice: ").strip()
        session = get_session()

        # ---------------- CUSTOMERS ----------------
        if choice == "1":
            name = input("Enter customer name: ").strip()
            email = input("Enter customer email: ").strip()
            customer = Customer(name=name, email=email)
            session.add(customer)
            session.commit()
            print("✅ Customer added successfully!")
            # Show updated table
            customers = session.query(Customer).all()
            table = [[c.id, c.name, c.email] for c in customers]
            print(tabulate(table, headers=["ID", "Name", "Email"], tablefmt="grid"))

        elif choice == "2":
            customers = session.query(Customer).all()
            if customers:
                table = [[c.id, c.name, c.email] for c in customers]
                print("\n📋 Customers Table:")
                print(tabulate(table, headers=["ID", "Name", "Email"], tablefmt="grid"))
            else:
                print("❌ No customers found.")

        elif choice == "3":
            customer_id = int(input("Enter customer ID to update: "))
            customer = session.query(Customer).get(customer_id)
            if customer:
                customer.name = input(f"New name ({customer.name}): ") or customer.name
                customer.email = input(f"New email ({customer.email}): ") or customer.email
                session.commit()
                print("✅ Customer updated!")
                # Show updated table
                customers = session.query(Customer).all()
                table = [[c.id, c.name, c.email] for c in customers]
                print(tabulate(table, headers=["ID", "Name", "Email"], tablefmt="grid"))
            else:
                print("❌ Customer not found.")

        elif choice == "4":
            customer_id = int(input("Enter customer ID to delete: "))
            customer = session.query(Customer).get(customer_id)
            if customer:
                session.delete(customer)
                session.commit()
                print("🗑️ Customer deleted!")
                # Show updated table
                customers = session.query(Customer).all()
                if customers:
                    table = [[c.id, c.name, c.email] for c in customers]
                    print(tabulate(table, headers=["ID", "Name", "Email"], tablefmt="grid"))
                else:
                    print("❌ No customers left.")
            else:
                print("❌ Customer not found.")

        # ---------------- BOOKINGS ----------------
        elif choice == "5":
            destination = input("Enter destination: ").strip()
            date = input("Enter date (YYYY-MM-DD): ").strip()
            customer_id = int(input("Enter customer ID for booking: "))

            customer = session.query(Customer).get(customer_id)
            if customer:
                booking = Booking(destination=destination, date=date, customer=customer)
                session.add(booking)
                session.commit()
                print("✅ Booking added successfully!")
                # Show updated table
                bookings = session.query(Booking).all()
                table = [[b.id, b.destination, b.date, b.customer.name] for b in bookings]
                print(tabulate(table, headers=["ID", "Destination", "Date", "Customer"], tablefmt="grid"))
            else:
                print("❌ Customer not found.")

        elif choice == "6":
            bookings = session.query(Booking).all()
            if bookings:
                table = [[b.id, b.destination, b.date, b.customer.name] for b in bookings]
                print("\n🗺️ Bookings Table:")
                print(tabulate(table, headers=["ID", "Destination", "Date", "Customer"], tablefmt="grid"))
            else:
                print("❌ No bookings found.")

        elif choice == "7":
            booking_id = int(input("Enter booking ID to delete: "))
            booking = session.query(Booking).get(booking_id)
            if booking:
                session.delete(booking)
                session.commit()
                print("🗑️ Booking deleted!")
                # Show updated table
                bookings = session.query(Booking).all()
                if bookings:
                    table = [[b.id, b.destination, b.date, b.customer.name] for b in bookings]
                    print(tabulate(table, headers=["ID", "Destination", "Date", "Customer"], tablefmt="grid"))
                else:
                    print("❌ No bookings left.")
            else:
                print("❌ Booking not found.")

        elif choice == "0":
            session.close()
            print("👋 Goodbye!")
            exit()

        else:
            print("❌ Invalid choice.")

