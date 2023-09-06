from faker import Faker
from datetime import datetime, timedelta
from sqlalchemy import create_engine,insert
from sqlalchemy.orm import sessionmaker
import random

from models import Booking, Customer, Room,room_customer
if __name__ == "__main__":
    fake = Faker()
    engine = create_engine('sqlite:///roombooking.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(Booking).delete()
    session.query(Customer).delete()
    session.query(Room).delete()
    session.query(room_customer).delete()

    customers = []
    for _ in range (20):
        customer= Customer(
            book_name=fake.name(),
            phone_number=fake.phone_number(),
            email=fake.email()
        )
        session.add(customer)
        customers.append(customer)

    rooms = []
    for _ in range (20):
        room = Room(
           
            room_number= random.randint(10,20),
            
            room_price=random.randint(100,200),
            room_capacity=random.randint(10,20)
            
        )
        session.add(room)
        rooms.append(room)