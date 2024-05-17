#!/usr/bin/python3
def safe_print_integer(value):
    """
    Print an integer using "{:d}".format().
    :param value: The value to print, can be any type
    :return: True if value is an integer and printed
    correctly, otherwise False
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
