#!/usr/bin/python3
"""json string type"""
import json


def to_json_string(my_obj):
    """function to_json_string

        Args:
            my_obj(any): obj file

        Return:
            the json like text
    """
    return (json.dumps(my_obj))
