# src/twende_travels/db/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Create SQLite database (it will generate a file named twende_travels.db)
engine = create_engine("sqlite:///twende_travels.db")

# Create a session factory
SessionLocal = sessionmaker(bind=engine)

# Base class for models to inherit from
Base = declarative_base()

# Dependency function (we’ll use this later)
def get_session():
    return SessionLocal()
