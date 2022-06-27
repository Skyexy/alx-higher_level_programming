#!/usr/bin/python3
"""
function that divides all elements of a matrix
"""
def matrix_divided(matrix, div):
    """function that divides all elements of a matrix
    """
    list2 = []
    listl = []
    round1 = 0
    if type (div) != (int or float):
        raise TypeError("div must be a number")
    if div == 0:
            raise ZeroDivisionError("division by zero")
    if type(matrix) == list:
        for row in matrix:
            if type(row) != list:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if len(row) == len(matrix[1]):
                for i in row:
                    if type(i) != (int or float):
                        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
                    else:
                        list2.append(round(i/div, 2))
                        listl.append(list2.copy())
                        list2.clear()
            else:
                raise TypeError("Each row of the matrix must have the same size")
    else:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    return listl
