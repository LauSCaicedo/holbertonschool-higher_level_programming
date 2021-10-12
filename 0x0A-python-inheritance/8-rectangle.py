#!/usr/bin/python3
'''
Write
a
class.
'''


class BaseGeometry():
    '''
    That raises an Exception.
    '''

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        self.value = value
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(self.name))
        if self.value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        super().integer_validator(width, height)
        if type(self.__height) is not int:
            raise TypeError("height must be an integer")
