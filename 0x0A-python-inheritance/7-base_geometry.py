#!/usr/bin/python3
"""This module creates a superclass"""


class BaseGeometry():
    """
    BaseGeometry class
    """

    def area(self):
        """
        Public instance method

        :param self:
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Public instance method

        :param self: main object
        :param name:
        :param value:
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
