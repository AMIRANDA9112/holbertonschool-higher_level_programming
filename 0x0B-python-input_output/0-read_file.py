#!/usr/bin/python3
"""This module open, read and print a file"""


def read_file(filename=""):
    """

    :param filename: file to print
    :return: void
    """
    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            print(line, end='')
