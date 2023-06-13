#!/usr/bin/python3
"""This module defines a class student"""


class Student:
    """A class representing a student"""

    def __init__(self, first_name, last_name, age):
        """Initializesa new stdudent"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Gets a dictionary representation of the stduent"""
        return self.__dict__
