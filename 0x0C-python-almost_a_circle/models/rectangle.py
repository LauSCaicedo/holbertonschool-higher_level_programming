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

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """return self"""
        return self.__width

    @width.setter
    def width(self, value):
        """to set it"""
        self.__width = value
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif self.__width <= 0:
            raise ValueError("width must be > 0")

    @property
    def height(self):
        """return self"""
        return self.__height

    @height.setter
    def height(self, value):
        """to set it"""
        self.__height = value
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif self.__height <= 0:
            raise ValueError("height must be > 0")

    @property
    def x(self):
        """return self"""
        return self.__x

    @x.setter
    def x(self, value):
        """to set it"""
        self.__x = value
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif self.__x < 0:
            raise ValueError("x must be >= 0")

    @property
    def y(self):
        """return self"""
        return self.__y

    @y.setter
    def y(self, value):
        """to set it"""
        self.__y = value
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif self.__y < 0:
            raise ValueError("y must be >= 0")
