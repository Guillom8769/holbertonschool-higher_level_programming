#!/usr/bin/python3

def element_at(my_list, idx):
    """
    Retrieve an element from a list by its index.

    Args:
        my_list (list): The list from which to retrieve the element.
        idx (int): The index of the element to retrieve.

    Returns:
        The element at the given index if the index is valid, None otherwise.
    """
    # Vérifie si l'index est négatif ou hors de la plage valide
    if idx < 0 or idx >= len(my_list):
        return None

    # Retourne l'élément à l'index spécifié
    return my_list[idx]
