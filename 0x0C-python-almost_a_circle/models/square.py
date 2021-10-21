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

    def update(self, *args, **kwargs):
        '''
            Method that assigns an argument to each attribute.
        '''
        if len(args) >= 1:
            for x, elemen_t in enumerate(args):
                if x == 0:
                    self.id = elemen_t
                if x == 1:
                    self.size = elemen_t
                if x == 2:
                    self.x = elemen_t
                if x == 3:
                    self.y = elemen_t

        else:
            for key, value in kwargs.items():
                if key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
                elif key == "id":
                    self.id = value

    def to_dictionary(self):
        '''
        Method that returns the dictionary representation.
        '''
        dic1 = ("id", "x", "size", "y")
        dic2 = (self.id, self.x, self.size, self.y)
        dic = dict(zip(dic1, dic2))
        return dic
