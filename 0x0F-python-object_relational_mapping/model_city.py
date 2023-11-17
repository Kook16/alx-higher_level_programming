#!/usr/bin/python3
''' python file that contains the class definition of a City and an instance
Base = declarative_base():'''

from model_state import Base
from sqlalchemy import String, Column, Integer, MetaData, ForeignKey


class City(Base):
    '''class with id and name attributes of each city'''
    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('State.id'), nullable=False)
