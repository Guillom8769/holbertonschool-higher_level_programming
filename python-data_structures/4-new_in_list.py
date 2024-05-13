#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    Replace an element in a list at a specific
      position without modifying the original list.

    Args:
        my_list (list): The original list.
        idx (int): Index at which to replace an element.
        element: New element to be placed at the specified index.

    Returns:
        list: A new list with the replaced element if the index
          is valid, otherwise a copy of the original list.
    """
    # Créer une copie de la liste originale
    list_copy = my_list[:]

    # Vérifier si l'index est dans une plage valide
    if 0 <= idx < len(list_copy):
        list_copy[idx] = element

    return list_copy
