#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    n = len(my_list) - 1
    list = my_list[:]
    if idx < 0 or idx > n:
        return list
    else:
        list[idx] = element
    return list
