#!/usr/bin/python3
"""
Model create
with the Class
Declaration
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """
    The atributes of database are created in this model
    and the conexion work from arguments pass and the (6-model_state.py) file
    """
    __tablename__ = "states"

    id = Column(Integer(), autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
