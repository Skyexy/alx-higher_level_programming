#!/usr/bin/python3
def common_elements(set_1, set_2):
    m = []
    for i in set_1:
        for z in set_2:
            if i in z:
                m.append(z)
                break
    return m
