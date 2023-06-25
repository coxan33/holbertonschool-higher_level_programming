#!/usr/bin/python3
"""1-my_list.py, tests/1-my_list.txt"""


class MyList(list):
    """My list Class"""

    def print_sorted(self):
        """ that prints the list, but sorted (ascending sort)"""
        print(sorted(self))
