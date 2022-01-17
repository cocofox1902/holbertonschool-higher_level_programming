#!/usr/bin/python3
def safe_print_integer(value):
    test = 1
    if type(value) == type(test):
        try:
            print("{}".format(value))
            return(True)
        except TypeError:
            return(False)
