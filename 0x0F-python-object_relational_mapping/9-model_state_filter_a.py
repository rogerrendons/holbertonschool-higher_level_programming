#!/usr/bin/python3
"""
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(argv[1], argv[2], argv[3]))
    
    Base.metadata.create_all(engine)
    session = Session(engine)

    for data in session.query(State).filter(State.name.like\
                                            ("%a%")).order_by(State.id):
        print("{}: {}".format(data.id, data.name))
    session.close()
