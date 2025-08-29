# src/twende_travels/cli/cli.py

from twende_travels.db.database import get_session
from twende_travels.models.models import Customer, Booking

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
        print("8. Exit")

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
            print("Goodbye! Thanks for using Twende Travels.")
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
    session.close()

    print(f"Booking to '{destination}' on {date} created for {customer.name}!")
    input("\nPress Enter to return to menu...")

def list_bookings():
    session = get_session()
    bookings = session.query(Booking).all()
    session.close()

    if bookings:
        print(f"\n Booking List ({len(bookings)} total):")
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
