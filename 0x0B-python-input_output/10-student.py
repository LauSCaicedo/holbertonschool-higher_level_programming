#!/usr/bin/python3
from typing import List


class Student:
    '''
    Public instance attributes.
    '''

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is list(str):
            return self.__dict__
