#!/usr/bin/python3
"""
Module 0-add_integer
Ce module fournit une fonction `add_integer` pour additionner deux entiers.
"""


def add_integer(a, b=98):
    """
    Additionne deux entiers ou flottants après les avoir convertis en entiers.
    Args:
        a (int, float): Le premier nombre à additionner.
        b (int, float): Le deuxième nombre à additionner. Par défaut à 98.

    Returns:
        int: La somme de `a` et `b` après les avoir convertis en entiers.

    Raises:
        TypeError: Si `a` ou `b` ne sont ni des entiers ni des flottants.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
