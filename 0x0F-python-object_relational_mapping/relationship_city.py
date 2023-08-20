#!/usr/bin/python3
"""module creates new table with orm"""
from sqlalchemy import Column, String, Integer, ForeignKey
from relationship_state import State, Base
from sqlalchemy.ext.declarative import declarative_base


class City(Base):
    """ class initate table to DB """
    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True, unique=True,
                primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
