#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    x = sorted(a_dictionary)
    for y in x:
        print(y, ": ", a_dictionary[y], '\n', end="")
