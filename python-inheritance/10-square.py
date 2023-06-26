#!/usr/bin/python3
"""10-square.py"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Write a class Square that inherits from Rectangle (9-rectangle.py)"""
    def __init__(self, size):
        """Instantiation with size"""
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """method must be implemented"""
        return self.__size ** 2
