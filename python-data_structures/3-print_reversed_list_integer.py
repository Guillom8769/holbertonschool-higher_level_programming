#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    Print all integers from a list in reverse order.
    Uses range() for reverse iteration and str.format() for printing integers.
    """
    for i in range(len(my_list) - 1, -1, -1):
        print("{:d}".format(my_list[i]))
