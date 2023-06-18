#!/usr/bin/python3
"""A module defining a base class"""


class Base:
    """A class defining base"""
    __nb__objects = 0

    def __init__(self, id=None):
        """A method initilizing id
        Args:
            id (int): The identity of the new Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb__objects += 1
            self.id = Base.__nb__objects
