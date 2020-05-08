#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    square_d = a_dictionary.copy()
    for key in square_d:
        square_d[key] *= 2
    return square_d
