#!/usr/bin/python3
"""Improve the files model_city.py and model_state.py, and
save them as relationship_city.py and relationship_state.py
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import City, Base


class State(Base):
    """Class State"""

    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True,
                primary_key=True, nullable=False, unique=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                          cascade='all, delete-orphan')