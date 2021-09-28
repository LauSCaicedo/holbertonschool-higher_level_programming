#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    long = 0
    number = 0

    for number in range(x):
        try:
            print("{:d}".format(my_list[number]), end="")
            long += 1
        except (TypeError, ValueError):
            pass
    print("")
    return long
