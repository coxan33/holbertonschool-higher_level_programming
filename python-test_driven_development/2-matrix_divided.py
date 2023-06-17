#!/usr/bin/python3
def matrix_divided(matrix, div):
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(error)

    if not all(isinstance(element, list) for element in matrix):
        raise TypeError(error)

    for x in matrix:
        if len(x) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    for x in matrix:
        for y in x:
            if not isinstance(y, (int, float)):
                raise TypeError(error)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new = list(matrix)

    for x in range(len(matrix)):
        new[x] = list(map(lambda x: round(x / div, 2), new[x]))
    return new
