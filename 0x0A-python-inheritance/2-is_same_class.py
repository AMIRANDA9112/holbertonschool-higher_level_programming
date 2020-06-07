# !/usr/bin/python3
"""This module check the class"""


def is_same_class(obj, a_class):
    """

            :param obj: class to verify
            :param a_class: point of compare
    """
    return type(obj) == a_class
