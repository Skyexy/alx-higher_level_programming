#!/usr/bin/python3
def safe_print_division(a, b):
    y = 0
    try:
        y = a / b
    except (ValueError, IndexError, ZeroDivisionError):
        y = None
    finally:
        print("Inside result: {}".format(y))
    return y
