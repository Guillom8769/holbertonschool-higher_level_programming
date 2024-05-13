#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """
    Prints all integers from a list, one per line.
    Args:
    my_list (list): A list of integers.
    """
    for number in my_list:
        print("{:d}".format(number))
