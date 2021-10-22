#!/usr/bin/python3
'''
creating a
first class
called (Base)
'''
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        l = []
        if list_objs is not None:
            for x in list_objs:
                l.append(cls.to_dictionary(x))
        filename = cls.__name__ + '.json'
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(l))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
        if cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + '.json'
        l = []
        try:
            with open(filename, 'r') as f:
                Rd = cls.from_json_string(f.read())
            for x, value in enumerate(Rd):
                l.append(cls.create(**Rd[x]))
        except:
            pass
        return l
