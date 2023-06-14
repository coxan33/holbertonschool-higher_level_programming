#!/usr/bin/python3
"""python3 -c 'print(__import__("my_module").__doc__)
'"""


class Square:
    """python3 -c 'print(__import__("my_module").MyClass.__doc__)'
    Square
    """

    def __init__(self, size=0):
        """python3 -c 'print(__import__("my_module").my_function.__doc__)'
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = size
