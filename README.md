#Twende Travels

Twende Travels is a simple **travel booking CLI application** built with **Python, SQLAlchemy, and SQLite**.  
It allows users to manage **customers** and their **bookings** directly from the command line.  

This project demonstrates:  
- Python project structuring (with `src/` and modules)  
- Using **SQLAlchemy ORM** to model and manage a database  
- Implementing CRUD (Create, Read, Update, Delete) functionality  
- Building a clean **command-line interface (CLI)**  

---

## Project Structure

Twende-Travels/
│
├── src/twende_travels/
│ ├── cli/ # CLI code
│ │ └── cli.py
│ │
│ ├── db/ # Database setup & connection
│ │ └── database.py
│ │
│ ├── models/ # ORM models (Customer, Booking)
│ │ └── models.py
│ │
│ ├── init.py
│
├── src/app.py # Entry point of the application
├── Pipfile # Pipenv dependencies
├── Pipfile.lock
├── requirements.txt # Exported dependencies
├── README.md # Project documentation
└── .gitignore # Git ignore rules

yaml
Copy code

---

## Setup & Installation

1. **Clone the repository**:
   ```sh
   git clone <your-repo-link>
   cd Twende-Travels
Install dependencies with Pipenv:

sh
Copy code
pipenv install
Run the app:

sh
Copy code
pipenv run python src/app.py
Features
Customers
Add a new customer (name + email)

List all customers

Update customer details

Delete a customer

Bookings
Add a booking (destination + date for a customer)

List all bookings

Delete a booking

 Other
Database setup happens automatically on startup

Organized menu system with clear sections

Proper error handling for invalid inputs

Database Design
Twende Travels uses SQLite for storage.
The database contains two tables:

customers
id	name	email
1	Mary Jane	mary@example.com
2	John Doe	john@example.com

bookings
id	destination	date	customer_id
1	Nairobi	2025-09-01	1
2	Mombasa	2025-09-05	2

 customer_id links each booking to a customer (relationship: one customer → many bookings).

Usage Example
markdown
Copy code
 Setting up the database...
 Database is ready!

Welcome to Twende Travels!

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
8. Exit
Example run:

yaml
Copy code
Enter choice: 1
Enter customer name: Mary Jane
Enter customer email: mary@example.com
 Customer 'Mary Jane' added successfully!
 Requirements
Python 3.8+

Pipenv (for environment + dependencies)

SQLAlchemy

Dependencies are managed in Pipfile, but also exported to requirements.txt for flexibility.

Author
Jennifer Nyambura.

