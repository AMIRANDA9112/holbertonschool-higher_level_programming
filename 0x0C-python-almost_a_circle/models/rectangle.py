#!/usr/bin/python3
"""
This module create a rectangle class
from base class
"""

from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter """
        return self.__width

    @width.setter
    def width(self, width):
        """ Setter """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ Getter """
        return self.__height

    @height.setter
    def height(self, height):
        """ Setter """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ Getter  """
        return self.__x

    @x.setter
    def x(self, x):
        """ Setter """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ Getter """
        return self.__y

    @y.setter
    def y(self, y):
        """ Setter """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ area method """
        return self.__width * self.__height

    def display(self):
        """ method that print a rectangle of '#' """
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """informal representation"""
        return ("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".
                format(self.id, self.__x, self.__y,
                       self.__width, self.__height))

    def update(self, *args, **kwargs):
        """ Updates multiple attributes. """
        if args:

            attributes = ['id', 'width', 'height', 'x', 'y']
            for count, item in enumerate(args):
                if count < 5:
                    setattr(self, attributes[count], item)

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """return a dictionary representation"""
        attributes = ['id', 'width', 'height', 'x', 'y']
        return {key: getattr(self, key) for key in attributes}
