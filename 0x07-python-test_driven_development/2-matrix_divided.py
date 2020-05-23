#!/usr/bin/python3
"""
matrix_divided
divide all elements of a matrix, only (int or float)
return matrix/div
"""
def matrix_divided(matrix, div):
    """
    div must be int or float, can'zero
    all arrows in matrix must be the same size
    max two decimals how rerturn in each matrix value
    """

    new_matrix = []

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) is not list or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")
    else:
        length = len(matrix[0])
    for arrow in matrix:
        if any(type(x) not in [int, float] for x in arrow):
            raise TypeError("matrix must be a matrix (list of lists)"
                        " of integers/floats")

        if len(arrow) is not length:
            raise TypeError("Each row of the matrix must have the same size")

        new_matrix.append(list(map(lambda x: round(x / div, 2), arrow)))

    return new_matrix
