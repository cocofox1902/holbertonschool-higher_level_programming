#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    test = 1
    for y in range(x):
        if type(my_list[y]) == type(test):
            try:
                print("{}".format(my_list[y]), end='')
                y += 1
            except IndexError:
                break
        else:
            exit
    print()
    return(y)
