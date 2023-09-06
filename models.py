from sqlalchemy import (create_engine,PrimaryKeyConstraint, Column,Integer,Date,String,ForeignKey,Table)
from sqlalchemy.orm import relationship,sessionmaker,backref
from sqlalchemy .ext.declarative import declarative_base
Base = declarative_base()
if __name__ == '__main__':
    engine = create_engine('sqlite:///roombooking.db',echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()

# Define the association table for the many-to-many relationship between Room and Customer
room_customer = Table(
   'room_customer',
    Base.metadata,
    Column('room_id', ForeignKey('rooms.id')),
    Column('customer_id', ForeignKey('customers.id')),
        extend_existing=True,
    
)

class Room(Base):
    __tablename__ = 'rooms'
    
    id= Column(Integer(),primary_key= True)
    room_number = Column (Integer())
    room_type = Column (String())
    room_capacity = Column (Integer())
    room_price = Column (Integer())
    bookings=relationship("Booking",backref=backref("room"))
    customers=relationship("Customer",secondary="room_customer",back_populates="rooms")
    
    def __repr__(self):
        return f'<Room id={self.id}, room_number={self.room_number}>'

    def is_available(self, check_in_date, check_out_date):
        bookings = self.bookings
        for booking in bookings:
            if (
                check_in_date < booking.check_out_date
                and check_out_date > booking.check_in_date
            ):
                return False
        return True
    def get_available_rooms(self, check_in_date, check_out_date):
        available_rooms = []
        for room in self.query.all():
            if room.is_available(check_in_date, check_out_date):
                available_rooms.append(room)
        return available_rooms
    
    
    def add_booking(self, customer, check_in_date, check_out_date):
        if self.is_available(check_in_date, check_out_date):
            booking = Booking(
                room_id=self.id,
                customer_id=customer.id,
                check_in_date=check_in_date,
                check_out_date=check_out_date
            )
            session.add(booking)
            session.commit()
            return booking
        else:
            return None

class Customer(Base):
    __tablename__ = 'customers'
    
    id= Column(Integer(),primary_key= True)
    book_name= Column(String())
    phone_number = Column(Integer())
    email = Column(String())
    bookings = relationship("Booking",backref="customer")
    rooms = relationship("Room", secondary="room_customer", back_populates="customers")



class Booking(Base):
   __tablename__ = 'bookings'

   id = Column(Integer(), primary_key=True)
   customer_id = Column(Integer(), ForeignKey('customers.id'))
   check_in_date = Column(Date)
   check_out_date = Column(Date)
   room_id= Column(Integer(), ForeignKey('rooms.id'))
   def __repr__(self):
        return f'<Booking id={self.id}, customer_id={self.customer_id}>'
    
    
   def get_duration(self):
        return (self.check_out_date - self.check_in_date).days
