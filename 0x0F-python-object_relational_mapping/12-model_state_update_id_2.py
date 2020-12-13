#!/usr/bin/python3
"""
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from sqlalchemy import literal

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(argv[1], argv[2], argv[3]),
                           )
    Base.metadata.create_all(engine)
    session = Session()

    q = session.query(State).filter(State.id == 2)
    record = q.one()
    record.name = 'New Mexico'
    session.flush()
    session.commit()
    session.close()
