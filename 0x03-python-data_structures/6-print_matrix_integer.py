#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    n = len(matrix)
    for i in range(0, n):
        y = len(matrix[i])
        for z in range(0, y):
            if z == (y - 1):
                print("{}".format(matrix[i][z]))
                continue
            print("{}".format(matrix[i][z]), end = " ")
