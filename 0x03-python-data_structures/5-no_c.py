#!/usr/bin/python3
def no_c(my_string):
    resuilt = ""
    for i in my_string:
        if i == 'c' or i == 'C':
            continue
        resuilt += i
    return resuilt
