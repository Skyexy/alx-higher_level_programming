#!/usr/bin/python3
def func(x):
    return x * x


def square_matrix_simple(matrix=[]):
    n = len(matrix)
    listf = []
    for i in range(0, n):
        r = list(map(func, matrix[i]))
        listf.append(r)
    return listf
