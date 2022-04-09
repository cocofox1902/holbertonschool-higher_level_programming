#!/usr/bin/python3

import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    new_engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                               .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(new_engine)
    Session = sessionmaker(bind=new_engine)
    session = Session()
    state = session.query(State).filter_by(name=argv[4]).first()
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")
    session.close()
