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
    matrix_b = matrix.copy()
    a = []
    b = []

    for i in matrix_b[0]:
        a.append(round(i/div, 2))

    for j in matrix_b[1]:
        b.append(round(j/div, 2))

    matrix_b = [a, b]
    return matrix_b
