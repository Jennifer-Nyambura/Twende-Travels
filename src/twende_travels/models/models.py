from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from twende_travels.db.database import Base

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)  # simple string for demo

    def __repr__(self):
        return f"<Account(id={self.id}, username='{self.username}')>"

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    bookings = relationship("Booking", back_populates="customer", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Customer(id={self.id}, name='{self.name}', email='{self.email}')>"

class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True)
    destination = Column(String, nullable=False)
    date = Column(String, nullable=False)

    customer_id = Column(Integer, ForeignKey("customers.id"))
    customer = relationship("Customer", back_populates="bookings")

    def __repr__(self):
        return f"<Booking(id={self.id}, destination='{self.destination}', date='{self.date}', customer_id={self.customer_id})>"
