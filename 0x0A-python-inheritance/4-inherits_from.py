#!/usr/bin/python3
"""module to test type"""


def inherits_from(obj, a_class):
    """ function inherits_from: test type

        Args:
            no Ags

        Return:
            type
    """
    if a_class is bool:
        return(False)
    if isinstance(obj, a_class) is True:
        return (type(obj), a_class)
