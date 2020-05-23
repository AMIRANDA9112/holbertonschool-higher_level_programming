# !/usr/bin/python3
"""
print_square
This function print a square with "#"
"""
def print_square(size):
    """

    :param size: size of square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    if size < 0:
        raise TypeError("size must be >= 0")

    for i in range(size):
        for j in range(size):
                print('#', end='')
        print()