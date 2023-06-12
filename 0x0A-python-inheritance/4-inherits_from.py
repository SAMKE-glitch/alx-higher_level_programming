#!/usr/bin/python3
"""
    A module that checks if an object is
    an instance of a class directly or
    inderectly from the specified class
"""


def inherits_from(obj, a_class):
    """
        A method that returns True if an object is an instance
        of a class that inherited directly or indirectly from
        specified  class
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
