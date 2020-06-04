#!/usr/bin/python3
""" Module that return a JSON representation of a object """
import json


def to_json_string(my_obj):
    """

    :param my_obj: object to JSON translation format
    :return: JSON representation
    """
    return json.dumps(my_obj)
