#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_divide(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
        matrix(list): A list of list of integers or floats.
        div(int or float): The divisor.

    Returns:
        list: A new matrix with elements divided by div, rounded to 2 decimals.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If each row of the matrix doesn't have the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix
    ):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/float")
    row_size = len(matrix[0]) if matrix else 0
    if any(len(row) != row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
