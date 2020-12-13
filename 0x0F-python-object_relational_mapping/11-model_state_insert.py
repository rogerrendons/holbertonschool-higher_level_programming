#!/usr/bin/python3
"""
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:\
                            3306/{}".format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    session = Session(engine)

    new_state = State(name="Miami")
    session.add(new_state)
    session.commit()
    state = session.query(State).order_by(State.id.desc()).first()
    print("{}".format(state.id))
    session.close()
