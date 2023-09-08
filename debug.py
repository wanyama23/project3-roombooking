import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Room,Booking,Customer
from sqlalchemy.ext.declarative import declarative_base

from faker import Faker
if __name__ == "__main__":
    
    engine = create_engine('sqlite:///roombooking.db',echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    fake=Faker()


# Start the debugging session
import ipdb;ipdb.set_trace()

