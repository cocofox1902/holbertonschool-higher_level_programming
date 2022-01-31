#!/usr/bin/python3
"""module of geometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangle

        function:
            def __init__
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
