#!/usr/bin/python3
"""module to show studen info"""


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

    def to_json(self):
        """function to_json

            Args:
                no args

            Return:
                dictinary of the thing
        """
        return(self.__dict__)
