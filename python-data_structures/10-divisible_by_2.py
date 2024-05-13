#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """
    Determine if each number in the list is divisible by 2.

    Args:
        my_list (list of int): The list of integers to check.

    Returns:
        list of bool: List indicating if each integer is divisible by 2.
    """
    # Création d'une liste pour stocker les résultats
    result = []
    # Parcourir chaque élément de la liste d'origine
    for number in my_list:
        # Ajouter True si le nombre est divisible par 2, sinon False
        result.append(number % 2 == 0)
    return result
