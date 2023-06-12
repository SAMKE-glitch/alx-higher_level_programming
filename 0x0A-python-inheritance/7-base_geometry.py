#!/usr/bin/python3
""" A module that defines a base geometry class BaseGeometry"""


class BaseGeometry:
    """ this class represents a base geometry"""

    def area(self):
        """An implemented area method"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
            Validates a value as an integer
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
