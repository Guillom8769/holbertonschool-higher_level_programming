#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    # Vérifier si l'indice est valide
    if idx < 0 or idx >= len(my_list):
        return my_list  # Rien ne change, retourne la même liste

    # Supprimer l'élément à l'indice spécifié
    del my_list[idx]

    return my_list
