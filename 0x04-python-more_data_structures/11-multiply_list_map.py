#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    sum = lambda x : x * number
    return list(map(sum, my_list))
