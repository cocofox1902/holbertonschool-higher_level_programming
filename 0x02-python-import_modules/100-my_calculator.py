#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    total = 0

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    if sys.argv[2] not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] == "+":
            total = a + b
        elif sys.argv[2] == "-":
            total = a - b
        elif sys.argv[2] == "*":
            total = a * b
        elif sys.argv[2] == "/":
            total = a / b


    print("{} {} {} = {}".format(a, sys.argv[2], b, total))
