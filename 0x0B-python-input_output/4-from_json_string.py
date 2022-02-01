#!/usr/bin/python3
"""module to print like json file"""
import json


def from_json_string(my_str):
    """function from_json_string

        Args:
            my_str(any): string to json like

        Return:
            the json like text
    """
    return (json.loads(my_str))
