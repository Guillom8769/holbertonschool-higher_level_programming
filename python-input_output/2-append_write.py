#!/usr/bin/python3


"""
Module 2-append_write
Defines a function that appends a string to a text file and returns
the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string to a text file (UTF8) and returns the number
    of characters added.

    Args:
        filename (str): The name of the file to append to. Default is an empty
        string.
        text (str): The text to append to the file. Default is an empty string.

    Returns:
        int: The number of characters added.
    """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
