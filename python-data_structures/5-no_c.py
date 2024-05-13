#!/usr/bin/python3

def no_c(my_string):
    """
    Remove all characters 'c' and 'C' from a string.
    Args:
        my_string (str): The string to process.
    Returns:
        str: A new string with all 'c' and 'C' characters removed.
    """
    filtered_string = ''.join([
        char for char in my_string
        if char not in ('c', 'C')
    ])
    return filtered_string
