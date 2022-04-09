#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    new_engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                               .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                               pool_pre_ping=True)
    Session = sessionmaker(bind=new_engine)
    session = Session()
    name_State = State(name="Louisiana")
    session.add(name_State)
    session.commit()
    print(name_State.id)
