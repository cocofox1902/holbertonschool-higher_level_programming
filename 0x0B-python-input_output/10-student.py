#!/usr/bin/python3
"""module to print info of a student"""


class Student:
    """class Student

        def __init__
        def to_json
    """
    def __init__(self, first_name, last_name, age):
        """function __init__

            Args:
                first_name(str): first name
                last_name(str): last name
                age(int): age

            Return:
                obj dictionary
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """function to_json

            Args:
                attrs(str): attributs

            Return:
                attributs to print
        """
        if (type(attrs) is list):
            return {x: self.__dict__.get(x) for x in attrs
                    if x in self.__dict__}
        return(self.__dict__)
