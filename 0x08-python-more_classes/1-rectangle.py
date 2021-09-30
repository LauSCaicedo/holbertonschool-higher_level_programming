#!/usr/bin/python3
"""calculate the square of a number"""


class Rectangle:
    """calculate the square of a number"""
    @property
    def width(self):
        """getter func"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter func"""
        self.__width = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise TypeError("size must be >= 0")

    @property
    def height(self):
        """getter func"""
        return self.__height

    @width.setter
    def height(self, value):
        """setter func"""
        self.__height = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise TypeError("size must be >= 0")

    def __init__(self, width=0, height=0):
        """Square class"""
        self.height = height
        self.width = width
