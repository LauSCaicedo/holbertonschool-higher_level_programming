#!/usr/bin/python3
"""
Write a class Student that defines
a student by and instantiation with
first_name, last_name and age
"""


class Student():
    """
    Create the class Student
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Public method that retrieves a dictionary
        representation of a Student instance
        """
        new_dic = {}
        if type(attrs) is list:
            for i in attrs:
                if type(i) is str and hasattr(self, i):
                    new_dic[i] = getattr(self, i)
                else:
                    pass
        else:
            new_dic = self.__dict__
        return new_dic
