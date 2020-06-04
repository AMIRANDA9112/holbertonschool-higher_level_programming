#!/usr/bin/python3
"""This module open, read and print a file in
a determinate number of lines"""


def read_lines(filename="", nb_lines=0):
    """

    :param nb_lines: limit to print
    :param filename: file to print
    :return: void
    """
    with open(filename, 'r', encoding="utf-8") as file:
        i = 0
        for line in file:
            print(line, end='')
            i += 1
            if i == nb_lines:
                return
