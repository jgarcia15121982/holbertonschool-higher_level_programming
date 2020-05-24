#!/usr/bin/python3


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix

    Args:
        matrix (int, float): The first parameter
        div (int, float): The second parameter

    Returns:
        All elements divided by div


    """
    if type(matrix) not in [int, float]:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix[0]) != len(matrix[1]):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in [int, float]:
        raise TypeError ("div must be a number")
    if div == 0
        raise ZeroDivisionError("division by zero")
    matrix_b = matrix.copy()
    a = []
    b = []

    for i in matrix_b[0]:
        a.append(round(i/div, 2))

    for j in matrix_b[1]:
        b.append(round(j/div, 2))

    matrix_b = [a, b]
    return matrix_b
