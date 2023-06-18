#!/usr/bin/python3
"""Rectangle"""


class Rectangle:
    """Rectangle"""

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height != 0 and self.__width != 0:
            return (self.__width * 2) + (self.__height * 2)
        else:
            return 0

    def print(self):
        if self.__height == 0 or self.__width == 0:
            return ""
        print(self)

    def __str__(self):
        words = ""
        if self.__height == 0 or self.__width == 0:
            return words
        for i in range(self.__height):
            words = words + ('#' * self.__width)
            words = words + ('\n' if i + 1 < self.__height else '')
        return words
