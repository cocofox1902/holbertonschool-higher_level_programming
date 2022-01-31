#!/usr/bin/python3
"""module of geometry"""

Rectangle = __import__('9-rectangle').Rectangle

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
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
