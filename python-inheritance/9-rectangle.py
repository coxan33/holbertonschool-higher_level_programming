#!/usr/bin/python3
"""9-rectangle.py"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Write a class Rectangle that inherits
    from BaseGeometry (7-base_geometry.py).
    (task based on 8-rectangle.py)"""
    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("heigth", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self) -> str:
        return f"[Rectangle] {self.__width}/{self.__height}"
