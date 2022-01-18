#!/usr/bin/python3
""" class Square """


class Square:
    """ def __init__
        def size
        def area
        def my_print
    """
    def __init__(self, size=0, position=(0, 0)):
        """ Init function

            Args:
                size (int): Size of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """position function

            Args:
                No arg

            Return:
                position of the square
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        if isinstance(value, tuple) is False or len(value) != 2 \
           or isinstance(value[0], int) is False or value[0] > 0 \
           or isinstance(value[1], int) is False or value[1] > 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ area function

            Args:
                No arg

            Return:
                area of the square
        """
        return(self.__size ** 2)

    def my_print(self):
        """ my_print function

            Args:
                No arg

            Return:
                print the square
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for j in range(0, self.__position[0]):
                print(" ", end="")
            for k in range(0, self.__size):
                print("#", end="")
            print()
