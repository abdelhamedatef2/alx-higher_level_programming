#!/usr/bin/python3
""" module  gets all states to contain 'a' in DB"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from model_state import State, Base
from sys import argv


def main():
    """func prevent run if imported as module"""
    engine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}\
                           @localhost:3306/{argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()
    rows = session.query(State).filter(State.name.like("%a%"))\
        .order_by(State.id).all()
    for row in rows:
        print(f"{row.id}: {row.name}")


if __name__ == "__main__":
    main()
