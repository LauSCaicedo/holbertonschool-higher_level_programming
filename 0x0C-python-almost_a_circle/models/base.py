#!/usr/bin/python3
'''
creating a
first class
called (Base)
'''


class Base:
    '''
    Methods
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
