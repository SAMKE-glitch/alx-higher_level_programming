#!/usr/bin/python3
"""A module defining a base class"""
import json
import csv
import turtle


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """
            Returns the JSON serialization of a list of dicts
            Args:
                list_dictionaries (list): A list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
