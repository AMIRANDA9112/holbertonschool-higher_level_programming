#!/usr/bin/python3
""" Module that save a object how a json file"""
import json


def save_to_json_file(my_obj, filename):
    """

    :param my_obj: object to save
    :param filename: file that save the object in JSON
    :return: void
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json.dumps(my_obj))
