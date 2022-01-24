#!/usr/bin/python3
""" class MagicClass """

import math


class MagicClass:
    """ def __init__
        def area
        def circumference
    """

    def __init__(self, radius=0):
        """ Init function

            Args:
                radius (int/float): Size of
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """ size function

            Return:
                number ^ 2 * pi
        """
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """ size function

            Return:
                2 * pi * number
        """
        return (2 * math.pi * self.__radius)
