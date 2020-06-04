#!/usr/bin/python3
"""This module defines the function that load a object from a json file"""

import json


def load_from_json_file(filename):
    """

    :param filename: JSON file
    :return: object
    """

    with open(filename, 'r', encoding='utf-8') as file:
        return json.loads(file.read())
