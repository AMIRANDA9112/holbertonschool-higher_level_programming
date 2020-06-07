#!/usr/bin/python3
"""This module creates a Class"""


class MyInt(int):
    """
    Int class
    """
    def __init__(self, number):
        self.number = number

    def __eq__(self, other):
        return self.number != other

    def __ne__(self, other):
        return other == self.number
