#!/usr/bin/python3
"""
    A module tha checks if an object is an instance
    of a class
"""


def is_same_class(obj, a_class):
    """ function that returns true if object is
        an instance of the class, otherwise false
    """
    return (type(obj) == a_class)
