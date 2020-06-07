#!/usr/bin/python3
"""This convert a object to dir output"""


def lookup(obj):
    """
    
    :param obj: object to convert
    :return: dir expresion of object
    """"
        return list(dir(obj))
