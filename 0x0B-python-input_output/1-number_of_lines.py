#!/usr/bin/python3
"""This module count the lines of a file"""


def number_of_lines(filename=""):
    """

    :param filename: file to print
    :return: number of lines
    """
    with open(filename, 'r', encoding="utf-8") as file:
        i = 0
        for line in file:
            i += 1
        return i
