#!/usr/bin/python3
"""module class of a rectangle"""


class Rectangle:
    """class rectangle
    """

    number_of_instances = 0
    print_symbol = "#"

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

    def bigger_or_equal(rect_1, rect_2):
        """ bigger_or_equal function

            Args:
                rect_1(rectangle): first rectangle
                rect_2(rectangle): second rectangle

            Return:
                bigger rectangle
        """
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return(rect_1)
        return(rect_2)

    def __str__(self):
        """ __str__ function

            Args:
                height(int/flaot): height of the rectangle
                width(int/flaot): width of the rectangle
                square(list): list of #
                print_symbol(str): symbol to print

            Return:
                a rectangle print
        """
        if self.__width == 0 or self.__height == 0:
            return("")
        square = []
        for i in range(self.__height):
            for j in range(self.__width):
                square.append("{}".format(str(self.print_symbol)))
            if self.__height - 1 != i:
                square.append("\n")
        return("".join(square))

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
