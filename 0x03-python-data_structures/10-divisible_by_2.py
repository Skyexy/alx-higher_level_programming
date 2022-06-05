#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    n = len(my_list)
    list = []
    for i in range(0, n):
        if my_list[i] % 2 == 0:
            list.append(True)
        else:
            list.append(False)
    return list
