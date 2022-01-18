#!/usr/bin/python3
""" class Square """


class Square:
    """ def __init__
        def size
        def area
    """
    def __init__(self, size=0):
        """ Init function

            Args:
                size (int): Size of the square
        """
        self.__size = size

    @property
    def size(self):
        """ size function

            Args:
                No arg

            Return:
                area of the square
        """
        return(self.__size)

    @size.setter
    def size(self, value):
        """ size function

            Args:
                value (int): value of the value
        """
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        return(value)

    def area(self):
        """ area function

            Args:
                No arg

            Return:
                area of the square
        """
        return(self.__size ** 2)
