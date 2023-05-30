#!/usr/bin/python3

"""module that defines a square """


class Square:
    """ A class that represents a square """

    def __init__(self, size=0):
        """ initialzing the square
        Args:
            size: represents the size of the square defined
        Raises:
            TypError: if the size isn't integer
            VelueError: if size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
