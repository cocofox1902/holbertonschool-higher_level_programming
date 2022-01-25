#!/usr/bin/python3
"""Module to add two integer
"""


def add_integer(a, b=98):
    """ add_integer function:
            Function to add two integerand return them

        Args:
            a(int/float): first to add
            b(int/float): second to add equal to 98 if not change

        Return:
            a + b
    """
    if (isinstance(a, (int, float)) is False):
        raise TypeError("a must be an integer")
    elif(isinstance(b, (int, float)) is False):
        raise TypeError("b must be an integer")
    return(int(a + b))
