#!/usr/bin/python3
""" Module comment """


class Square:
    """ def __init__ """
    def __init__(self, size=0):
        """ Init function

            Args:
                size (int): Size of the square
        """
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
