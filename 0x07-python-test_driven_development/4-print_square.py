#!/usr/bin/python3
'''
Function that prints
a square with
the character #.
'''


def print_square(size):
    '''
    size of square
    '''
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size is float and size < 0:
        raise TypeError("size must be an integer")
    for x in range(size):
        for z in range(size):
            print("#", end="")
        print("")
