from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column,Integer,Date,String,ForeignKey,Table)
engine = create_engine('sqlite:///roombooking.db')

Base = declarative_base()