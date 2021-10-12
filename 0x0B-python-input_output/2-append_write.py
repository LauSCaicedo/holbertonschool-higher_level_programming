#!/usr/bin/python3
'''
Function that appends a string at the
end of a text file (UTF8)
and returns the number of characters added.
'''


def append_write(filename="", text=""):
    '''
    Use the with statement.
    '''
    with open(filename, 'a', encoding='UTF8') as f:
        af = f.write(text)
        return af
