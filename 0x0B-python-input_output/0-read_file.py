#!/usr/bin/python3
""" This modolue defines a text file reading method"""


def read_file(filename=""):
    """Method that reads a content of utf-8 text file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
