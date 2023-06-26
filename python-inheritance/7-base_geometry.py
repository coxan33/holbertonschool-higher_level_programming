#!/usr/bin/python3
"""6-base_geometry.py"""


class BaseGeometry:
    """Write an empty class BaseGeometry"""
    def area(self):
        """Write a class BaseGeometry (based on 5-base_geometry.py)."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
