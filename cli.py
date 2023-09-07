import click
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models import Customer, Room,Booking
Base = declarative_base()
engine=create_engine("sqlite:///roombooking.db")
Session = sessionmaker(bind=engine)
session = Session()
@click.group()
def cli():
    pass
@cli.command()
@click.option("--book_name", prompt="enter book name")
@click.option("--phone_number", prompt="enter phone number")
@click.option("--email", prompt="enter email")
def add_customer(book_name, phone_number, email):
    customer = Customer(book_name=book_name, phone_number=phone_number, email=email)
    session.add(customer)
    session.commit()
    print("Customer added successfully")