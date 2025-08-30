# Twende Travels CLI

Twende Travels is a **Python command-line application** for managing a travel agency's customers and bookings. It provides a **user-friendly CLI interface** with authentication, customer management, and booking management. Data is displayed neatly in **tables** using the `tabulate` library.

This project is ideal for beginners learning **Python**, **SQLAlchemy**, and **building interactive CLI applications**.

---

## Features

### Authentication
- Register a new account
- Login with existing credentials
- Menu-based navigation

### Customer Management
- Add Customer: Enter name and email
- List Customers: Display all customers in a table
- Update Customer: Edit customer details
- Delete Customer: Remove customers

### Booking Management
- Add Booking: Link a booking to a customer by ID
- List Bookings: Display bookings in a table including customer name
- Delete Booking: Remove a booking by ID

### Interactive CLI
- Clear, numbered menus
- Automatic table display after each operation
- Immediate feedback on success or errors

---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/YOUR_USERNAME/Twende-Travels.git
cd Twende-Travels
Install dependencies

Using pipenv:

bash
Copy code
pipenv install
pipenv shell
Or using pip:

bash
Copy code
pip install sqlalchemy tabulate
Run the application:

bash
Copy code
pipenv run python src/app.py
Usage
Authentication Menu
markdown
Copy code
--- Authentication ---
1. Register
2. Login
0. Exit
Enter choice:
Register a new account or login with an existing account.

Main Menu
markdown
Copy code
✨ Welcome to Twende Travels ✨

--- Customers ---
1. Add Customer
2. List Customers
3. Update Customer
4. Delete Customer

--- Bookings ---
5. Add Booking
6. List Bookings
7. Delete Booking

--- Exit ---
0. Exit
Quick Start Example
Run the application:

bash
Copy code
pipenv run python src/app.py
Register a new account:

yaml
Copy code
Enter choice: 1
Choose a username: Alice
Choose a password: password123
✅ Account created for 'Alice'
Login with the account:

yaml
Copy code
Enter choice: 2
Username: Alice
Password: password123
✅ Welcome back, Alice!
Add a customer:

sql
Copy code
Enter choice: 1
Enter customer name: Bob
Enter customer email: bob@email.com
✅ Customer added successfully!

📋 Customers Table:
+----+------+------------------+
| ID | Name | Email            |
+----+------+------------------+
| 1  | Bob  | bob@email.com    |
+----+------+------------------+
Add a booking:

sql
Copy code
Enter choice: 5
Enter destination: Mombasa
Enter date (YYYY-MM-DD): 2025-09-10
Enter customer ID for booking: 1
✅ Booking added successfully!

🗺️ Bookings Table:
+----+------------+------------+----------+
| ID | Destination| Date       | Customer |
+----+------------+------------+----------+
| 1  | Mombasa    | 2025-09-10 | Bob      |
+----+------------+------------+----------+
List all bookings:

sql
Copy code
Enter choice: 6

🗺️ Bookings Table:
+----+------------+------------+----------+
| ID | Destination| Date       | Customer |
+----+------------+------------+----------+
| 1  | Mombasa    | 2025-09-10 | Bob      |
+----+------------+------------+----------+
Exit the application:

yaml
Copy code
Enter choice: 0
👋 Goodbye!
💡 Tip: After every operation (add/update/delete), the app automatically prints the updated table for easy reference.

Database
Built with SQLAlchemy ORM

Stores Customer and Booking models

Each booking is linked to a customer (one-to-many relationship)

Models:

python
Copy code
class Customer(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

class Booking(Base):
    id = Column(Integer, primary_key=True)
    destination = Column(String)
    date = Column(String)
    customer_id = Column(Integer, ForeignKey('customer.id'))
    customer = relationship('Customer')
Project Structure
graphql
Copy code
Twende-Travels/
│
├── src/
│   ├── app.py              # Entry point
│   └── twende_travels/
│       ├── cli/
│       │   └── cli.py      # CLI menus and logic
│       ├── db/
│       │   └── database.py # Database connection
│       └── models/
│           └── models.py   # SQLAlchemy models
│
├── Pipfile / requirements.txt
├── README.md
└── .gitignore
Dependencies
Python 3.8+

SQLAlchemy

tabulate

Install dependencies:

bash
Copy code
pip install -r requirements.txt
Contributing
Contributions are welcome! You can:

Add new features

Improve CLI usability

Enhance table formatting

Add unit tests

License
This project is licensed under the MIT License.

yaml
Copy code
