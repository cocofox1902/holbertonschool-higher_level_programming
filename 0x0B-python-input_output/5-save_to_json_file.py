#!/usr/bin/python3
"""module to save as a json file"""
import json


def save_to_json_file(my_obj, filename):
    """function save_to_json_file

        Args:
            my_obj(any): obj type
            filename(str): file name

        Return:
            no return
    """
    with open(filename, 'w') as f:
        lines = json.dumps(my_obj)
        f.writelines(lines)
    f.close()
