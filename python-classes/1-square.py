#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)
'"""


class Square:
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    Square
    """

    __size = 0

    def __init__(self, size):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)'
        """
        self.__size = size
