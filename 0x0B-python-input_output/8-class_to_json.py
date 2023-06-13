#!/usr/bin/python3
"""This module defines a python class-toJSON function"""


def class_to_json(obj):
    """Returns dictionary representation of a simple data structure"""
    return obj.__dict__
