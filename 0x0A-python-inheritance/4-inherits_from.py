#!/usr/bin/python3
"""module to test type"""


def inherits_from(obj, a_class):
    """ function inherits_from: test type

        Args:
            no Ags

        Return:
            type
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
