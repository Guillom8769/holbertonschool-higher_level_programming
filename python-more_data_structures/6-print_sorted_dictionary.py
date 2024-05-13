#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    Print the keys and values of a dictionary sorted by the keys.
    Assumes all keys are strings and only sorts the first level keys.
    :param a_dictionary: The dictionary to print
    """
    # Trier les clés du dictionnaire par ordre alphabétique
    for key in sorted(a_dictionary.keys()):
        # Imprimer chaque clé suivie de sa valeur correspondante
        print(f"{key}: {a_dictionary[key]}")
