#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    key_del = []
    for key in a_dictionary:
        if a_dictionary[key] == value:
            key_del.append(key)
    for key in key_del:
        del a_dictionary[key]
    return a_dictionary
