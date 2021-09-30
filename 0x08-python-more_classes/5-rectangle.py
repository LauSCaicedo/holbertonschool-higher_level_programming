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
            raise ValueError("width must be >= 0")

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
            raise ValueError("height must be >= 0")

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        stringe = ""
        if self.__width == 0 or self.__height == 0:
            return stringe
        else:
            for x in range(self.__height):
                for z in range(self.__width):
                    stringe += "#"
                if z != self.__width and x != self.__height:
                    if (x + 1) != self.__height:
                        stringe += '\n'
            return stringe

    def __repr__(self):
        Rect = 'Rectangle(' + str(self.__width) + \
            ', ' + str(self.__height) + ')'
        return Rect

    def __del__(self):
        print("Bye rectangle...")
