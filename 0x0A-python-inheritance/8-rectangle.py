#!/usr/bin/python3
"""
    A module that defines a Rectangle class that inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that inherits from BaseGeometry class"""

    def __init__(self, width, height):
        """Method that initilizesa new Rectangle"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
