#!/usr/bin/python3
"""This module add attributes"""


def add_attribute(obj, name, value):



    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    elif hasattr(obj, "__slots__") and not hasattr(obj, name):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
