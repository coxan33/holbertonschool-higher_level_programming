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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        area = self.__size * self.__size
        return area

    def my_print(self):
        if self.__size == 0:
            print()
        for _ in range(self.__size):
            print('#' * self.__size)
