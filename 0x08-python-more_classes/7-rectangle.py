#!/usr/bin/python3
"""
create Rectangle class
"""


class Rectangle():
    """
    Rectangle define
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """

        :type width: int
        must be >= 0
        :type height: int
        must be >= 0
        """
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def area(self):
        """
        returns area
        :return: area
        :rtype: int
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        returns perimeter:
        :return: perimeter:
        :rtype: int
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

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

    def __str__(self):
        """

        :return: return string how rectangle with "#"
        :type: str
        """
        hashtag_str = ""
        if self.width != 0 and self.__height != 0:
            hashtag_str = hashtag_str + \
                          "\n".join(str(self.print_symbol) *
                                    self.__width for j in range(self.__height))
        return hashtag_str

    def __repr__(self):
        """returns a representation """
        repre = "Rectangle(" + str(self.__width) + ", " \
                + str(self.__height) + ")"
        return (repre)

    def __del__(self):
        """message for delete classes"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
