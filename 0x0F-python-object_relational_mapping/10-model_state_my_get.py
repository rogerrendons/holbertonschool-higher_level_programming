#!/usr/bin/python3
""" Script print State object passed as argument from the database """

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    for data in session.query(State).filter_by(name=argv[4]):
        print(data.id)
        exit()
    print("Not found")
    session.close()
