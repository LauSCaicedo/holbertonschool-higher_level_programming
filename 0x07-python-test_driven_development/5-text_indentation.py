#!/usr/bin/python3
'''
Function that prints a text with
2 new lines after each of
these characters: ., ? and :
'''


def text_indentation(text):
    '''
    text for index
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in range(len(text)):
        if text[i] == ".":
            print(".")
            print()
        elif text[i] == "?":
            print('?')
            print()
        elif text[i] == ":":
            print(":")
            print()
        else:
            if (text[i] == " " and (text[i - 1]
                                    in ".?:" or text[i - 1] == " ")):
                continue
            print("{}".format(text[i]), end="")
