from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column,Integer,Date,String,ForeignKey,Table)
from sqlalchemy.orm import relationship,sessionmaker,backref

Base = declarative_base()

if __name__ == '__main__':
    engine = create_engine('sqlite:///roombooking.db')
    Session = sessionmaker(bind=engine)
    session = Session()