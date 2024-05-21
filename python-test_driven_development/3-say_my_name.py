#!/usr/bin/python3
"""
Module 3-say_my_name
Ce module fournit une fonction `say_my_name` pour afficher un nom complet.
"""


def say_my_name(first_name, last_name=""):
    """
    Affiche "My name is <first name> <last name>".

    Args:
        first_name (str): Le prénom.
        last_name (str): Le nom de famille.

    Raises:
        TypeError: Si first_name ou last_name ne sont pas
        des chaînes de caractères.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
