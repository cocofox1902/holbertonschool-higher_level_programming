#!/usr/bin/python3
"""module to append in a file"""


def append_write(filename="", text=""):
    """function append_write

        Args:
            filename(str): file name
            text(str): text to append

        Return:
            the lenght of the text
    """
    with open(filename, 'a') as f:
        f.writelines(text)
    f.close()
    return(len(text))
