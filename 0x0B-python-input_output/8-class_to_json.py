#!/usr/bin/python3
"""module to return the dictionary"""


def class_to_json(obj):
    """function class_to_json

        Args:
            obj(str): obj

        Return:
            obj dictionary
    """
    return(obj.__dict__)
