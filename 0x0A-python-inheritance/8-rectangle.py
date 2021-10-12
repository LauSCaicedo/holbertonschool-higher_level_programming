#!/usr/bin/python3
'''
Importing
the Base
Geometric class
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    Class Rectangle that inherits.
    '''

    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator('width', width)
        self.integer_validator('height', height)
