#!/usr/bin/python3
"""module class of a rectangle"""


class Rectangle:
    """class rectangle
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ __init__ function

            Args:
                width(int/flaot): width of the rectangle
                height(int/flaot): height of the rectangle

            Return:
                No return
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

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
        if value < 0:
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
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ area function

            Args:
                height(int/flaot): height of the rectangle
                width(int/flaot): width of the rectangle

            Return:
                area of the rectangle
        """
        return(self.__width * self.__height)

    def perimeter(self):
        """ perimeter function

            Args:
                height(int/flaot): height of the rectangle
                width(int/flaot): width of the rectangle

            Return:
                perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return(0)
        return((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """ __str__ function

            Args:
                height(int/flaot): height of the rectangle
                width(int/flaot): width of the rectangle
                square(list): list of #

            Return:
                a rectangle print
        """
        if self.__width == 0 or self.__height == 0:
            return("")
        square = []
        for i in range(self.__height):
            for j in range(self.__width):
                square.append("#")
            if self.__height - 1 != i:
                square.append("\n")
        return("".join(square))

    def __repr__(self):
        """ __repr__ function

            Args:
                height(int/flaot): height of the rectangle
                width(int/flaot): width of the rectangle
                tuple(tuple): tuple of height and width

            Return:
                a rectangle print
        """
        tuple = (self.__width, self.__height)
        return("Rectangle{}".format(tuple))

    def __repr__(self):
        """ __repr__ function

            Args:
                No Agrs

            Return:
                rectangle
        """
        rect = "Rectangle(" + str(self.__width) + ","
        rect += str(self.__height) + ")"
        return rect

    def __del__(self):
        """ __del__ function

            Args:
                No Agrs

            Return:
                No Return
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
