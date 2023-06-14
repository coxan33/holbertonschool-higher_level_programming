#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        i = 0
        for y in x:
            print("{:d}".format(y), end="" if len(x) - 1 == i else " ")
            i += 1
        print()
