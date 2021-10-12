#!/usr/bin/python3
def read_file(filename=""):
    with open(filename) as f:
        Rd = f.read()
        print(Rd, end="")
    f.close()
