#!/usr/bin/python3
"""module to write in a file"""


def write_file(filename="", text=""):
    """function write_file

        Args:
            filename(str): file name
            text(str): text to write

        Return:
            the lenght of the text
    """
    with open(filename, 'w') as f:
        f.writelines(text)
    f.close()
    return(len(text))
