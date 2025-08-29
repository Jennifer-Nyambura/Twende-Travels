# src/app.py

from twende_travels.db.database import Base, engine
from twende_travels.models.models import Customer, Booking
from twende_travels.cli.cli import main_menu

def setup_database():
    """Create database tables if they don’t exist."""
    print("Setting up the database...")
    Base.metadata.create_all(engine)
    print("Database is ready!")

if __name__ == "__main__":
    setup_database()
    main_menu()
