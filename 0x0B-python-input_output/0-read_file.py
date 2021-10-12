#!/usr/bin/python3
'''
function that reads a
text file (UTF8) and
prints it to stdout
'''


def read_file(filename=""):
    '''
    Use the with statement.
    '''
    with open(filename, encoding='UTF8') as f:
        Rd = f.read()
        print(Rd, end="")
    f.close()
