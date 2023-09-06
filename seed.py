from faker import Faker
from datetime import datetime, timedelta
from sqlalchemy import create_engine,insert
from sqlalchemy.orm import sessionmaker
import random

from models import Booking, Customer, Room,room_customer
if __name__ == "__main__":
    