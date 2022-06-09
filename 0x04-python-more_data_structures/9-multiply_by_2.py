#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_values = sorted(a_dictionary.items())
    dic = {}
    for k, y in new_values:
        dic[k] = y * 2
    return (dic)
