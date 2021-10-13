#!/usr/bin/python3
"""
class Rectangle that inherits from BaseGeometry (7-base_geometry.py).
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
        Type class of Rectangle inherit BaseGeometry
    """

    def __init__(self, width, height):
        """
        Constructor Magic method
        """

        self.__width = width
        self.__height = height
        self.integer_validator('width', width)
        self.integer_validator('height', height)

    def area(self):
        return (self.__width * self.__height)

    def __str__(self):
        return (f"[Rectangle] {self.__width}/{self.__height}")
