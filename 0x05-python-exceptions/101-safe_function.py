#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        total = fct(*args)
        return(total)
    except (ZeroDivisionError, IndexError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
