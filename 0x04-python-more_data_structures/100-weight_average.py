#!/usr/bin/python3
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return 0

    coef = 0
    size = 0
    total = 0
    for l in my_list:
        coef = coef + (l[0] * l[1])
        size = size + l[1]
        total = coef / size
    return (total)
