#!/usr/bin/python3
"""
This is the "2-matrix_divided" module.
The module functions: matrix_divided(a, b).
"""


def matrix_divided(matrix, div):
    """
    matrix_divided: function that divides all elements of a matrix
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    """
    size = None
    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for ele in matrix:
        if type(ele) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if size is None:
            size = len(ele)
        elif size != len(ele):
            raise TypeError("Each row of the matrix must have the same size")
        for i in ele:
            if type(i) is not int and type(i) is not float:
                raise TypeError(
                        "matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(i / div, 2) for i in ele] for ele in matrix]
