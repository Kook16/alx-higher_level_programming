#!/usr/bin/python3
'''script 14-model_city_fetch_by_state.py that prints all City objects
from the database hbtn_0e_14_usa'''
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]
        ), pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State, City).filter(City.state_id == State.id).\
        order_by(City.id).all()

    for result in results:
        print(f"{result.State.name}: ({result.City.id}) {result.City.name}")
