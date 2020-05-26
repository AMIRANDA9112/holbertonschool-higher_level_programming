#!/usr/bin/python3
"""
create Rectangle class
"""


class Rectangle(object):
    """
    Rectangle class
    """
    def __init__(self, width=1, height=1):

        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("widthe must be >= 0")
        self.width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be >= 0")
        self.height = height

    @property
    def area(self):

        return self.width * self.height
