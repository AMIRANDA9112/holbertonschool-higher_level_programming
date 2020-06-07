#!/usr/bin/python3
"""This module checks if is subclass of other"""


def inherits_from(obj, a_class):
    """

    :param obj: suspect of parent
    :param a_class: suspect of inherit
    :return: true or false
    """
    if type(obj) is not a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
