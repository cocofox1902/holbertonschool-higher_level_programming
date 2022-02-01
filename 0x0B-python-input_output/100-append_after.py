#!/usr/bin/python3
"""module to append after"""


def append_after(filename="", search_string="", new_string=""):
    """function append_after

        Args:
            filename(str): file name
            search_string(str): thing to search
            new_string(str): the new string

        Return:
            no return
    """
    result = ""
    with open(filename, 'r') as f:
        for lines in f:
            result += lines
            if search_string in lines:
                result += new_string
    with open(filename, 'w') as w:
        w.write(result)
