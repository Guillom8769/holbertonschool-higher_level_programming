#!/usr/bin/python3

"""
Module that defines a function to return the dictionary description
with simple data structure for JSON serialization of an object.
"""


def class_to_json(obj):
    """
    Function that returns the dictionary description with simple data
    structure (list, dictionary, string, integer and boolean) for JSON
    serialization of an object.

    Args:
        obj: An instance of a Class.

    Returns:
        dict: The dictionary description of the object.
    """
    return obj.__dict__
