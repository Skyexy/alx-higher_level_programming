#!/usr/bin/python3
"""List all State objects that contain letter 'a' from db 'hbtn_0e_6_usa'
Script should take 3 args: username, pw, and db name
"""
import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    sl = session.query(State, City).filter(State.id == City.state_id)
    for q in sl:
        print("{}: ({:d}) {}".format(q.State.name, q.City.id, q.City.name))
