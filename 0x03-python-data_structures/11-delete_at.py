#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    n = len(my_list) - 1
    if idx > (n) or idx < 0:
        return my_list
    else:
        for i in range(0, n + 1):
            if i == idx:
                del(my_list[i])
    return my_list
