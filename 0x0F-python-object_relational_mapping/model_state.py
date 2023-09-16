#!/usr/bin/python3
''' python file that contains the class definition of a State and an instance
Base = declarative_base():'''
from sqlalchemy import Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base

metadata = MetaData()
Base = declarative_base(metadata=metadata)


class State(Base):
    '''class with id and name attributes of each state'''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
