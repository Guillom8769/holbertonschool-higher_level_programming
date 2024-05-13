#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    Print a matrix of integers.

    Args:
        matrix (list of list of int): The matrix to print.
    """
    for row in matrix:
        # Imprimer chaque ligne en utilisant `str.format()
        print(' '.join("{:d}".format(num) for num in row))
