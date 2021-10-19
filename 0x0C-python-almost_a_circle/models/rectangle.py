#!/usr/bin/python3
'''
creation of another
class that inherits
the class (Base).
'''
from models.base import Base


class Rectangle(Base):
    '''
    Methods
    '''
    super().__init__(id)

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
