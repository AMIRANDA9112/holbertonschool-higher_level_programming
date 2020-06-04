#!/usr/bin/python3
""" this module return a object how a dictionary"""


def class_to_json(obj):
    """

    :param obj: object to convert
    :return: dictionary
    """
    return obj.__dict__
