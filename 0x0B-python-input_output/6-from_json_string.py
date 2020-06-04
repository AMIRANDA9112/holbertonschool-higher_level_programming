#!/usr/bin/python3
""" Module that return in JSON format a string input"""
import json


def from_json_string(my_str):
    """

    :param my_str: string to translate a JSON format
    :return: JSON format
    """
    return json.loads(my_str)
