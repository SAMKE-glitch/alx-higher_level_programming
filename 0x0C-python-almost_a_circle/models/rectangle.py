#!/usr/bin/python3
"""A module defining a Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """
        Class Rectangle implements Base.
        Methods:
            __init__()
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initiliazes instance of the class"""

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
            getter function for __width
            Returns: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            setter method for width
            Args:
            value (int): value to be set.
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
            getter function for height
            Returns: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            setter function for height
            Args:
                value (int): value to be set as
        """
        if type(value) != int:
            raise TypeError("Height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @property
    def x(self):
        """
            getter function for x
            Returns: x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
            setter function for x
            Args:
                value (int) value to be set
        """
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")

        self.__x = value

    @property
    def y(self):
        """
            getter function for y
            Returns: y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
            setter function for y
            Args:
                value (int): value to be set
        """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value
