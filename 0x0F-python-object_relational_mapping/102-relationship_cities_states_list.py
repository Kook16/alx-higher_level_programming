#!/usr/bin/python3
'''a script that lists all State objects, and corresponding City objects,
    contained in the database hbtn_0e_101_usaa'''
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]
        ), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).order_by(State.id).all()
    for state in result:
        for city in state.cities:
            print(f'{city.id}: {city.name} -> {state.name}')

    session.close()
