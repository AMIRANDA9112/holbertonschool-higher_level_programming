#!/usr/bin/python3
"""This module create a sub class of rectangle subclass"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):

    """Square class"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):

        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
