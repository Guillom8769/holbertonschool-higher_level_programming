#!/usr/bin/python3
"""
Module 4-print_square
Ce module fournit une fonction `print_square` pour
imprimer un carré avec le caractère #.
"""


def print_square(size):
    """
    Imprime un carré avec le caractère #.

    Args:
        size (int): La taille du côté du carré.

    Raises:
        TypeError: Si la taille n'est pas un entier.
        ValueError: Si la taille est inférieure à 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
