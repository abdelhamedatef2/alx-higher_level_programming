#!/usr/bin/python3
""" module get states from DB by provided name"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from model_state import State, Base
from sys import argv


def main():
    """func make script not run if imported as module"""
    engine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}\
                           @localhost:3306/{argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(State).filter(State.name == argv[4]).first()
    if rows:
        print(rows.id)
    else:
        print("Not found")


if __name__ == "__main__":
    main()
