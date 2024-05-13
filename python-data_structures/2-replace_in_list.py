#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    Replace an element in a list at a specific index with a new element.

    Args:
        my_list (list): The list to modify.
        idx (int): The index at which to replace an element.
        element (any): The new element to insert at the specified index.

    Returns:
        list: The modified list if the index is valid,
        otherwise the original list.
    """
    # Vérifie si l'index est dans une plage valide
    if 0 <= idx < len(my_list):
        my_list[idx] = element
    return my_list
