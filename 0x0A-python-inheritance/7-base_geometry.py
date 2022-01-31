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
