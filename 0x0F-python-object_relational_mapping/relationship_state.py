#!/usr/bin/python3
""" module makes state table using ORM """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """ clase makes state tables inherit from
        decleraive base
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False,
                unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")
