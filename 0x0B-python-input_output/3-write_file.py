#!/usr/bin/python3
""" This module write a string ina file"""


def write_file(filename="", text=""):
    """

    :param text: string to write in file
    :type filename: text file
    """
    with open(filename, 'w', encoding="utf-8") as file:
        file.write(text)
    file.close()
    return len(text)
