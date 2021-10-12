#!/usr/bin/python3
'''
Function that writes a string
to a text file (UTF8) and returns
the number of characters written.
'''


def write_file(filename="", text=""):
    '''
    Use the with statement.
    '''
    with open(filename, 'w', encoding='UTF8') as f:
        Wt = f.write(text)
    return Wt
