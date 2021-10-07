#!/usr/bin/python3
'''
Function
that adds
2 integers.
'''


def add_integer(a, b=98):
    '''
    a and b are integers
    '''
    if type(a) is float:
        a = int(a)
    if type(a) is not int:
        raise TypeError("a must be an integer")
    if type(b) is float:
        b = int(b)
    if type(b) is not int:
        raise TypeError("b must be an integer")
    return a + b
