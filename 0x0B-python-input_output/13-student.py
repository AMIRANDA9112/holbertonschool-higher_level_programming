#!/usr/bin/python3
""" This module create the student class and convert it in dictionary, and set the object create"""


class Student:
    """
    Student class
    """

    def __init__(self, first_name, last_name, age):
        """Public instance attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """

        :param attrs:  list to convert in a dictionary
        :return: dictionary
        """
        if attrs is not None:
            new_dict = {}
            for i in attrs:
                if i in self.__dict__:
                    new_dict[i] = self.__dict__[i]
            return new_dict
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """

        :param json: student to set
        :return: student set
        """
        for key in json:
            self.__dict__[key] = json[key]
