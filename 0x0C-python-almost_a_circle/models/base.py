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

    @staticmethod
    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """
        if json_string is None or json_string == "":
            return []

        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Returns all attributes already set. """
        if cls.__name__ is "Rectangle":
            dummy = cls(2, 4)
        elif cls.__name__ is "Square":
            dummy = cls(2)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """l
        """
        file_name = cls.__name__ + ".json"
        my_list = []
        if not os.path.isfile(file_name):
            return my_list
        with open(file_name) as my_file:
            data = cls.from_json_string(my_file.read())
            for instance in data:
                my_list.append(cls.create(**instance))
        return my_list

