#!/usr/bin/python3
"""This module create a base class"""
import json
import csv


class Base():
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """

        :param id: int how id for all child class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """list of dictionaries to JSON format"""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        my_dict = json.dumps(list_dictionaries)
        return my_dict

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Have a JSon string of a list of objects
        how a representation on a file
        """
        dic_list = []
        if list_objs is not None:
            for item in list_objs:
                dic_list.append(cls.to_dictionary(item))
        with open(cls.__name__ + ".json", "w") as file:
            file.write(cls.to_json_string(dic_list))
