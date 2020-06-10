#!/usr/bin/python3
"""
This module create a rectangle class
from base class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """informal representation"""
        return ("[Square] ({:d}) {:d}/{:d} - {:d}".
                format(self.id, self.x, self.y,
                       self.width))

    @property
    def size(self):
        """Getter"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Updates multiple attributes. """
        if args:

            attributes = ['id', 'size', 'x', 'y']
            for count, item in enumerate(args):
                if count < 4:
                    setattr(self, attributes[count], item)

        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """return a dictionary representation"""
        attributes = ['id', 'size', 'x', 'y']
        return {key: getattr(self, key) for key in attributes}
