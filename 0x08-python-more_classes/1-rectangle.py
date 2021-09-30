#!/usr/bin/python3
"""calculate the Rectangle of a number"""


class Rectangle:
    """calculate the Rectangle of a number"""

    def __init__(self, width=0, height=0):
        """Rectangle class"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter func"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter func"""
        self.__width = value
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")

    @property
    def height(self):
        """getter func"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter func"""
        self.__height = value
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
