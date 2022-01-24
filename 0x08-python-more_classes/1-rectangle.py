#!/usr/bin/python3
"""module class of a rectangle"""


class Rectangle:
    """class rectangle
    """
    def __init__(self, width=0, height=0):
        """ __init__ function

            Args:
                width(int/flaot): width of the rectangle
                height(int/flaot): height of the rectangle

            Return:
                No return
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """ width function

            Args:
                width(int/flaot): width of the rectangle

            Return:
                width
        """
        return(self.__width)

    @width.setter
    def width(self, value):
        """ width function test value

            Args:
                width(int/flaot): width of the rectangle

            Return:
                no return
        """
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ height function

            Args:
                height(int/flaot): height of the rectangle

            Return:
                height
        """
        return(self.__height)

    @height.setter
    def height(self, value):
        """ height function test value

            Args:
                height(int/flaot): height of the rectangle

            Return:
                no return
        """
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
