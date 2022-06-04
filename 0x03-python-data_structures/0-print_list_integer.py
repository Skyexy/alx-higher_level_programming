#!/usr/bin/python3
def print_list_integer(my_list=[]):
    n = len(my_list) - 1
    for i in range(0, n + 1):
        print("{:d}".format(my_list[i]))
