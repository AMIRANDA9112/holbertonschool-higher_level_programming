#!/usr/bin/python3
"""this module create class Square"""


class Square():
    """Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """ Verifying type of value, size and position"""

        self.size = size
        try:
            self.position = position
        except TypeError as err:
            print(err)

    @property
    def position(self):
        """ Return the position """
        return self.__position

    @position.setter
    def position(self, value):
        if (type(value) != tuple or len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

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

    def area(self):
        """return square of size how area"""
        return self.__size ** 2

    def my_print(self):
        """ Print a square with # """

        if self.__size == 0:
            pass

        for i in range(self.__position[1]):
            pass

        for i in range(self.__size):
            for j in range(self.__size + self.__position[0]):
                if j < self.__position[0]:
                    print(' ', end='')
                else:
                    print('#', end='')
            print()