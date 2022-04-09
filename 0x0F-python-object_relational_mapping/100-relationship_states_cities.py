#!/usr/bin/python3
"""
Improve the files model_city.py and model_state.py, and save
them as relationship_city.py and relationship_state.py"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.schema import Table

if __name__ == "__main__":
    new_engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]),
                                   pool_pre_ping=True)
    Base.metadata.create_all(new_engine)

    session = Session(new_engine)
    new_city = City(name='San Francisco')
    new = State(name='California')
    new.cities.append(new_city)
    session.add_all([new, new_city])

    session.commit()
    session.close()