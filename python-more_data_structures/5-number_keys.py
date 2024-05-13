#!/usr/bin/python3
def number_keys(a_dictionary):
    """
    Return the number of keys in the dictionary `a_dictionary`.
    :param a_dictionary: A dictionary from which to count the keys
    :return: The number of keys in the dictionary
    """
    # Obtenir le nombre de clés en utilisant len() sur les clés du dictionnaire
    return len(a_dictionary.keys())
