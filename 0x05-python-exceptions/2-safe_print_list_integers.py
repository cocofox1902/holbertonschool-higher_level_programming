#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    test = 1
    for y in range(0, x):
        try:
            print("{:d}".format(my_list[y]), end='')
            y += 1
        except IndexError:
            continue
    print()
    return(y)
