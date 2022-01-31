#!/usr/bin/python3
"""module of geometry"""


class BaseGeometry:
    """class BaseGeometry

        function:
            def area
            def integer_validator
    """
    def area(self):
        """function area

            Args:
                no agrs

            Return:
                no return
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function integer_validator

            Args:
                name(string): name of it
                value(int): number upper of 0

            Return:
                no return
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """class Rectangle

        function:
            def __init__
            def __str__
            def area
    """
    def __init__(self, width, height):
        """function __init__

            Args:
                width(int): width of the rectangle
                height(int): height of the rectangle

            Return:
                no return
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """function __str__

            Args:
                no args

            Return:
                The rectangle value
        """
        return("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))

    def area(self):
        """function area

            Args:
                no args

            Return:
                area of the rectangle
        """
        return(self.__width * self.__height)


class Square(Rectangle):
    """class Square

        function:
            def __init__
            def area
    """
    def __init__(self, size):
        """function __init__

            Args:
                no args

            Return:
                no return
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
