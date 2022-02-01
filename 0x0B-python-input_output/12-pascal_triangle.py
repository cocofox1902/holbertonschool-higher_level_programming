#!/usr/bin/python3
"""module to print pascal triangle"""


def pascal_triangle(n):
    """function pascal_triangle

        Args:
            n(str): row of the triangle

        Return:
            what to print
    """
    if n <= 0:
        return []

    pascal = [[1]]

    while len(pascal) != n:
        triangle = pascal[-1]
        tmp = [1]
        lenght = len(triangle)
        for i in range(lenght - 1):
            tmp.append(triangle[i] + triangle[i + 1])
        tmp.append(1)
        pascal.append(tmp)

    return (pascal)
