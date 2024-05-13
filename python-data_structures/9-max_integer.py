#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    Find the largest integer in a list.

    Args:
        my_list (list): The list of integers to evaluate.

    Returns:
        int: The largest integer in the list, or None if the list is empty.
    """
    # Vérifier si la liste est vide
    if not my_list:
        return None
    # Initialiser la valeur maximale avec le premier élément de la liste
    max_value = my_list[0]
    # Parcourir les éléments de la liste à partir du deuxième élément
    for number in my_list[1:]:
        if number > max_value:
            max_value = number

    return max_value
