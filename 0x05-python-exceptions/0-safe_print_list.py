#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    long = 0
    while long < x:
        try:
            print("{}".format(my_list[long]), end="")
        except IndexError:
            break
        long += 1
    print("")
    return long
