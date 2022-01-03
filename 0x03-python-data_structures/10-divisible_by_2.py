#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list = my_list.copy()
    for i in range(len(my_list)):
        if my_list[i] % 2:
            list[i] = False
        else:
            list[i] = True
    return(list)
