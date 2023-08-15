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

    def to_json(self):
        """
        retrieves a dictionary representation of a Student
        """
        return self.__dict__
