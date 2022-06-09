#!/usr/bin/python3
def uniq_add(my_list=[]):
    i = 0
    mem = []
    for z in my_list:
        m = 0
        for d in mem:
            if z == d:
                m = 1
                break
        mem.append(z)
        if m == 0:
            i = i + z
    return i
