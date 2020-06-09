# !/usr/bin/python3
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
