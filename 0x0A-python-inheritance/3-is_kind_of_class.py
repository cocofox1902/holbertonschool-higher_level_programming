#!/usr/bin/python3
"""module to test type"""


def is_kind_of_class(obj, a_class):
    """ function is_kind_of_class: test type

        Args:
            no Ags

        Return:
            type
    """
    if isinstance(obj, a_class) is True:
        return (type(obj), a_class)
