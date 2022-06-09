#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    new_values = a_dictionary.items()
    dic = {}
    m = " "
    z = 0
    for k, y in new_values:
        if z < y:
            z = y
            m = k
    return m
