#!/usr/bin/python3
"""
create Rectangle class
"""


class Rectangle ():
    """
    Rectangle define
    """
    def __init__(self, width=0, height=0):
        """

        :type width: int
        must be >= 0
        :type height: int
        must be >= 0
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """

        :return: __height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """

        :param height: int must be >= 0
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """

        :return: __width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """

        :param width: int must be >= 0
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width
