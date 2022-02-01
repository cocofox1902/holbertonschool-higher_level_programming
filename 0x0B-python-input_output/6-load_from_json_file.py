#!/usr/bin/python3
"""module to load as a jason file"""
import json


def load_from_json_file(filename):
    """function load_from_json_file

        Args:
            filename(str): file name

        Return:
            json laod of the line read
    """
    with open(filename) as f:
        lineread = f.read()
    f.close()
    return(json.loads(lineread))
