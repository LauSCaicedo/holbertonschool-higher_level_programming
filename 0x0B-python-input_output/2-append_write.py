#!/usr/bin/python3
def append_write(filename="", text=""):
    with open(filename, 'a', encoding='UTF8') as f:
        af = f.write(text)
        return af
