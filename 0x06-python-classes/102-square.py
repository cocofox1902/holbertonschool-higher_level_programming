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

    def area(self):
        """ area function

            Args:
                No arg

            Return:
                area of the square
        """
        return(self.__size ** 2)

    def __eq__(self, other):
        """ __eq__ function

            Args:
                No arg

            Return:
                comparaison
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """ __ne__ function

            Args:
                No arg

            Return:
                comparaison
        """
        return self.area() != other.area()

    def __le__(self, other):
        """ __le__ function

            Args:
                No arg

            Return:
                comparaison
        """
        return self.area() <= other.area()

    def __ge__(self, other):
        """ __ge__ function

            Args:
                No arg

            Return:
                comparaison
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """ __lt__ function

            Args:
                No arg

            Return:
                comparaison
        """
        return self.area() < other.area()

    def __gt__(self, other):
        """ __gt__ function

            Args:
                No arg

            Return:
                comparaison
        """
        return self.area() > other.area()
