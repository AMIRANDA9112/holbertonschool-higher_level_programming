#!/usr/bin/python3
"""this module create a list with the triangle pascal sequence"""


def pascal_triangle(n):
    """

    :param n: limit of triangle
    :return: list with the pascal triangle sequence
    """
    triangle = []
    row = []
    prev_row = []
    for i in range(0, n + 1):
        row = [j > 0 and j < i - 1 and i > 2 and prev_row[j - 1] + prev_row[j] or 1 for j in range(0, i)]
        prev_row = row
        triangle += [row]
    return triangle[1:]
