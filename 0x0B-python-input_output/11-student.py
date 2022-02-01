#!/usr/bin/python3
"""module to print student info"""


class Student:
    """class Student

        def __init__
        def to_json
        def reload_from_json
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

    def reload_from_json(self, json):
        """function reload_from_json

            Args:
                json(str): set attribut

            Return:
                no return
        """
        for x, y in json.items():
            setattr(self, x, y)
