#!/usr/bin/python3
"""module to add attribute"""


def add_attribute(obj, name, what):
    """function add_attribute

            Args:
                no args
            Return:
                no return
        """
    if hasattr(obj, '__dict__') is False:
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, what)
