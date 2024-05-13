#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Add all unique integers in the list `my_list`.
    :param my_list: List of integers
    :return: The sum of all unique integers
    """
    # Convertir la liste en un ensemble pour éliminer les doublons
    unique_numbers = set(my_list)
    # Calculer la somme de tous les entiers uniques
    total = sum(unique_numbers)
    return total
