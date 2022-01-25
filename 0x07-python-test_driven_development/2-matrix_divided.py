#!/usr/bin/python3
"""Module to divided an all matrix
"""


def matrix_divided(matrix, div):
    """ matrix function:
            Function to divided an all matrix

        Args:
            matrix(list): the list of list to divided
            div(int/float): the divider

        Return:
            the matrix with all the value divided by div
    """
    if not matrix or isinstance(matrix, list) is False or matrix is None:
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")
    for line in matrix:
        if isinstance(line, list) is False:
            raise TypeError("matrix must be a matrix (list of lists) of "
                            "integers/floats")
    for i in matrix:
        if len(matrix[0]) != len(matrix[1]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if isinstance(j, (float, int)) is False:
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")
            if isinstance(div, (int, float)) is False:
                raise TypeError("div must be a number")
            if div == 0:
                raise ZeroDivisionError("division by zero")
    return[[float(format(j / div, '.2f')) for j in i] for i in matrix]
