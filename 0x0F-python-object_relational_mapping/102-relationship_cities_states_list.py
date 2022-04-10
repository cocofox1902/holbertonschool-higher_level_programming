#!/usr/bin/python3
"""Write a script that lists all City objects
from the database hbtn_0e_101_usa"""

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
    for city in session.query(City).order_by(City.id).all():
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    session.close()
