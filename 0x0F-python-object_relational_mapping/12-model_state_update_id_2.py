#!/usr/bin/python3
"""
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                            argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    session = Session(engine)

    for state in session.query(State).filter_by(id=2):
        state.name = "New Mexico"
    session.commit()
    session.close()
