#!/usr/bin/python3
""" module make state table with ORM """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """ clase makes state tables inherit from
        declerive base class
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False,
                unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
