#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    size = len(sys.argv)
    if size != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        operator = sys.argv[2]
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if operator == "+":
            print("{} {} {} = {}".format(a, operator, b, add(a, b)))
            sys.exit(0)
        elif operator == "-":
            print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
            sys.exit(0)
        elif operator == "*":
            print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
            sys.exit(0)
        elif operator == "/":
            print("{} {} {} = {}".format(a, operator, b, div(a, b)))
            sys.exit(0)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
