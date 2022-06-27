#!/usr/bin/python3
"""
Module 4-print_square
Contain one method that the size must be integr and greater than zero
Print square with the character #
"""


def print_square(size):
    """Print square with character #"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    else:
        message = "\n".join(["#" * size for i in range(size)])
        print(message)
