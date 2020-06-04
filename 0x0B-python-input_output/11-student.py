#!/usr/bin/python3
""" This module create the student classs"""


class Student:
    """
    Student class
    """

    def __init__(self, first_name, last_name, age):
        """Public instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Public method that retrieves a dictionary """
        return self.__dict__
