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

    @property
    def size(self):
        """to return size of Square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter size of square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """ Print a square with # """
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print("#" * self.size)
