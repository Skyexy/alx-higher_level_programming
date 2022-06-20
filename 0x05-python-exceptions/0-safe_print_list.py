#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    y = 0
    for i in range(0, x):
        try:
            print("{:d}".format(list[i]), end="")
            y += 1
        except (ValueError, IndexError):
            pass
    print("")
    return y
