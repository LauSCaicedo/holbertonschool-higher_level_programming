#!/usr/bin/python3
"""
print a sorted
list from a class
previously added
"""


class MyList(list):
    """
    sort the list
    """

    def print_sorted(self):
        print(sorted(self))
