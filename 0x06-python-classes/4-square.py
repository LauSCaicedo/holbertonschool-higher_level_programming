#!/usr/bin/python3
"""calculate the square of a number"""


class Square:
    """calculate the square of a number"""
    @property
    def size(self):
        """getter func"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter func"""
        self.__size = value
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise TypeError("size must be >= 0")

    def __init__(self, size=0):
        """Square class"""
        self.__size = size

    def area(self):
        """take the square of a nimber"""
        return self.__size ** 2
