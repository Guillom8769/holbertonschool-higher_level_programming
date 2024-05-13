#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """
    Supprime un élément à une position spécifique dans une liste.

    Args:
        my_list (list): La liste dont un élément sera supprimé.
        idx (int): L'indice de l'élément à supprimer.

    Returns:
        list: La liste modifiée après la suppression de l'élément.
    """
    # Vérifier si l'indice est valide
    if 0 <= idx < len(my_list):
        # Supprimer l'élément en utilisant le découpage de liste
        my_list = my_list[:idx] + my_list[idx+1:]

    return my_list
