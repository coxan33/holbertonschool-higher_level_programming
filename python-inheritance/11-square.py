#!/usr/bin/python3
"""11-square.py"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Write a class Square that inherits from Rectangle
    (9-rectangle.py). (task based on 10-square.py"""
    def __init__(self, size):
        """Instantiation with size"""
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ method must be implemented"""
        return self.__size ** 2

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
