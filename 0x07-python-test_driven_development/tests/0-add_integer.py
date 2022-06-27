#!/usr/bin/python3
"""
a function that adds 2 integers
"""

def add_integer(a, b=98):
    """a function that adds 2 integers
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("a must be an integer")
    if type(a) == float:
        a = int(a)
    elif type(b) == float:
        b = int(b)
    return (a + b)
