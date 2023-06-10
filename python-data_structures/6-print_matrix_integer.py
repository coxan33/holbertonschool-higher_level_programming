#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    x = '\n'.join([''.join(['{:3}'.format(item) for item in y]) for y in matrix])
    print(x)
