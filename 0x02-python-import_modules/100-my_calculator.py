#!/usr/bin/python3
def main():
    from calculator_1 import add, sub, mul, div
    import sys
    n = len(sys.argv)-1
    if n != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    y = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if y == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif y == '/':
        print("{} / {} = {}".format(a, b, div(a, b)))
    elif y == '+':
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif y == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)


if __name__ == "__main__":
    main()
