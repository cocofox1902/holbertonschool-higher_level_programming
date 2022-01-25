#!/usr/bin/python3
"""Module to say a name
"""


def say_my_name(first_name, last_name=""):
    """ say_my_name function:
            Function to say a name

        Args:
            first_name(str): the first name
            last_name(str): the last name

        Return:
            the name introduced by a sentence
    """
    if isinstance(first_name, str) is False:
        raise TypeError("first_name must be a string")
    if isinstance(last_name, str) is False:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
