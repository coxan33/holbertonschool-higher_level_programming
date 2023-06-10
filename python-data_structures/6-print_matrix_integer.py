#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    x = '\n'.join([''.join(['{:3}'.format(a) for a in y]) for y in matrix])
    print(x)
