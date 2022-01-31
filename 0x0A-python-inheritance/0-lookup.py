#!/usr/bin/python3
"""module to list all of available attributes and methods of an object"""


def lookup(obj):
    """ function lookup: to list available attributes and methods of an object

        Args:
            no Ags

        Return:
            list
    """
    return(dir(obj))
