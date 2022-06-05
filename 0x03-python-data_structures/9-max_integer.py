#!/usr/bin/python3
def max_integer(my_list=[]):
    n = len(my_list)
    if n == 0:
        return None
    else:
        for i in range(0, n):
            for j in range(i, n):
                if my_list[i] < my_list[j]:
                    break
                if (j == n - 1):
                    return my_list[i]
