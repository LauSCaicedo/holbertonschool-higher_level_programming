#!/usr/bin/python3
'''
Creation of another
class that inherits
the class (Rectangle).
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''
    Init constructor.
    '''

    def __init__(self, size, x=0, y=0, id=None):
        '''
        Call the super class.
        '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''
            Method to convert to a string.
        '''
        return (f"[{self.__class__.__name__}] \
({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """return self"""
        return self.width

    @size.setter
    def size(self, value):
        """to set it"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
