#!/usr/bin/python3
'''
Write a class
Student that
defines a student.
'''


class Student:
    '''
    Public instance attributes.
    '''

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        ''' attrs is a list of strings, only attribute
        names contained in this list must be retrieved
        '''
        new_dic = {}
        if type(attrs) is list:
            for i in attrs:
                if type(i) is str and hasattr(self, i):
                    new_dic[i] = getattr(self, i)
                else:
                    pass
        else:
            new_dic = self.dict
        return new_dic
