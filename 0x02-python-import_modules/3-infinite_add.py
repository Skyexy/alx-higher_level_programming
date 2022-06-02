#!/usr/bin/python3
import sys
if __name__ == "__main__":
    n = len(sys) - 1
    for i in range(1, n + 1):
        y = int(sys.argv[i])
        m = m + y
    print("{}".format(m))
