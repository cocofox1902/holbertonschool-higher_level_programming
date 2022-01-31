#!/usr/bin/python3
"""module"""


class MyInt(int):
    """ class MyInt

        def __eq__
        def __ne__
    """
    def __eq__(self, dif):
        """function __eq__

            Args:
                no Args

            Return:
                Diference
        """
        return int(self) != dif

    def __ne__(self, dif):
        """function __eq__

            Args:
                no Args

            Return:
                Equal
        """
        return int(self) == dif
