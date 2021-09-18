#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    exe = sorted(a_dictionary)
    for i in exe:
        print("{}: {}".format(i, a_dictionary[i]))
