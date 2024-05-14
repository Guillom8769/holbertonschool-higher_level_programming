#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """
    Return a new dictionary with all values multiplied by 2.
    :param a_dictionary: Dictionary with integer values
    :return: A new dictionary with values multiplied by 2
    """
    # Créer un nouveau dictionnaire pour stocker les résultats
    new_dict = {}
    # Itérer sur chaque paire clé-valeur dans le dictionnaire original
    for key, value in a_dictionary.items():
        # Multiplier la valeur par 2 et l'ajouter au nouveau dictionnaire
        new_dict[key] = value * 2
    return new_dict
