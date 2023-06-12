#!/usr/bin/python3
"""
    A module that has a class Mylist that
    inherits from a class list
"""


class MyList(list):
    """A class that inherits from the list"""
    def print_sorted(self):
        """Method that prints a sorted list"""
        print(sorted(self))
