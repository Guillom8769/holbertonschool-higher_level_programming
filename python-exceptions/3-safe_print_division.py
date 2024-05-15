#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Divide two integers and print the result.
    :param a: Dividend (integer)
    :param b: Divisor (integer)
    :return: The result of the division,
    or None if division by zero
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
