#!/usr/bin/python3
"""module creates a new state with city """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sys import argv


def main():
    """func not run when imported as module"""
    engine = create_engine(f"mysql+mysqldb://{argv[1]}:{argv[2]}\
                           @localhost:3306/{argv[3]}")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    row = State(name="California", cities=[City(name="San Francisco")])
    session.add(row)
    session.commit()
    session.close()


if __name__ == "__main__":
    main()
