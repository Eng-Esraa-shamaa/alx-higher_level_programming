#!/usr/bin/python3
"""
defining class Student that defines a student
"""


class Student:
    """
    defining student class
    """
    def __init__(self, first_name, last_name, age):
        """
        Args:
            first_name: the first name of student
            last_name: last name of student
            age: age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves a dictionary representation of a Student
        Args:
            attrs: attribute names
        """
        if not isinstance(attrs, list):
            return self.__dict__
        for i in attrs:
            if not isinstance(i, str):
                return self.__dict__
        str_dict = {}
        for string in attrs:
            if string in self.__dict__.keys():
                str_dict[string] = self.__dict__[string]
        return str_dict

    def reload_from_json(self, json):
        """
        Args:
            json: the json
        """
        for i, j in json.items():
            setattr(self, i, j)
