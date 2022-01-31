#!/usr/bin/python3
"""module to sort a list"""


class MyList(list):
    def __init__(self, number=list()):
        """ function __init__

        Args:
            no Ags

        Return:
            no Return
    """
        self.list = list(number)

    def print_sorted(self):
        """ function print_sorted: sort a list

        Args:
            sort

        Return:
            no return
    """
        print("{}".format(sorted(self)))
