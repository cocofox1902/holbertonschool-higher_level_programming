#!/usr/bin/python3
"""module to read a file"""


def read_file(filename=""):
    """function read_file

        Args:
            filename(str): file name

        Return:
            no return
    """
    with open(filename, 'r') as f:
        lines = f.read()
        f.close()
    print(lines)
