#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Return the key with the biggest integer value in
    the dictionary `a_dictionary`.
    If no score is found, return None.
    :param a_dictionary: Dictionary with integer values
    :return: The key with the highest value, or None if
    the dictionary is empty or None
    """
    if not a_dictionary:
        return None

    # Initialiser les variables pour stocker la clé avec la plus grande valeur
    best_key = None
    best_value = float('-inf')  # Valeur initiale très basse

    # Itérer sur chaque paire clé-valeur dans le dictionnaire
    for key, value in a_dictionary.items():
        if value > best_value:
            best_value = value
            best_key = key

    return best_key
