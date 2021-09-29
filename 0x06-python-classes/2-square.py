#!/usr/bin/python3
"""
Define class called (Square).
"""


class Square:
    """
    Define class (Square).
    """

    def __init__(self, size=0):
        """
        Private instance attribute (Size).
        """
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise TypeError("size must be >= 0")
