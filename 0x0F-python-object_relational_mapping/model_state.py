#!/usr/bin/python3
''' python file that contains the class definition of a State and an instance
Base = declarative_base():'''
from sqlalchemy.orm import declarative_base
from sqlalchemy import String, Column, Integer, MetaData

metadata = MetaData()
Base = declarative_base(metadata=metadata)


class State(Base):
    '''class with id and name attributes of each state'''
    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
