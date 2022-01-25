#!/usr/bin/python3
"""Module to print a square
"""


def print_square(size):
    """ print_square function:
            Function to print a square

        Args:
            size(int/float): the size of the square

        Return:
            a square
    """
    if isinstance(size, int) is False:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
