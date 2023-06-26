#!/usr/bin/python3
"""8-rectangle.py"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """"Write a class Rectangle that inherits
    from BaseGeometry (7-base_geometry.py)."""
    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.integer_validator("width", width)
        __width = width
        self.integer_validator("heigth", height)
        __height = height
