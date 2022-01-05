#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    return({n: 2 * a_dictionary[n] for n in a_dictionary.keys()})
