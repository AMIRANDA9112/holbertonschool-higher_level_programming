#!/usr/bin/python3
""" This module append a string in a file"""


def append_write(filename="", text=""):
    """

    :param text: string to append in file
    :type filename: text file
    """
    with open(filename, 'a', encoding="utf-8") as file:
        file.write(text)
    file.close()
    return len(text)
