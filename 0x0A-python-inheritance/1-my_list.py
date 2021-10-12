#!/usr/bin/python3
'''
Class MyList
that inherits
from list.
'''


class MyList(list):
    '''
    Prints the list, but sorted (ascending sort).
    '''

    def print_sorted(self):
        print(sorted(self))
