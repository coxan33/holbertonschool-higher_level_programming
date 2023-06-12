#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    x = list(matrix)
    for y in range(len(matrix)):
        x[y] = list(map(lambda x: x ** 2, x[y]))
    return x
