#!/usr/bin/python3
"""this module create class Square"""


class Square():
    """Square class"""
    def __init__(self, size=0):
        """size: size of square"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        """Function area(size)"""

    def area(self):
        """return square of size how area"""
        return self.__size**2
