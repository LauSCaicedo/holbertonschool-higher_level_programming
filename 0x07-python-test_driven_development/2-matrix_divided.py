#!/usr/bin/python3
'''
function that divides
all elements
of a matrix.
'''


def matrix_divided(matrix, div):
    '''
    Matrix, list of list, div, integer for divide
    '''
    Counter = len(matrix[0])

    if isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for x in matrix:
        newlist = []
        for i in x:
            if len(x) != Counter:
                raise TypeError(
                    "Each row of the matrix must have the same size")
            ar = isinstance(i, (int, float))
            if ar is False:
                raise TypeError(
                    "matrix must be a matrix"
                    "(list of lists) of integers/floats")
            newlist.append(round(i/div, 2))
        new_matrix.append(newlist)
    return new_matrix
