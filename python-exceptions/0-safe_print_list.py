#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    Print x elements of a list.
    :param my_list: List of elements
    :param x: Number of elements to print
    :return: The number of elements printed
    """
    count = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            count += 1
        except IndexError:
            break
    print()
    return count
