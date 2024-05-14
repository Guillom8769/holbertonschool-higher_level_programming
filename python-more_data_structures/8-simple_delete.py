#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Delete a key in the dictionary `a_dictionary`.
    If the key exists, it will be deleted. If the key doesn't exist,
    the dictionary remains unchanged.
    :param a_dictionary: Dictionary from which to delete a key
    :param key: Key to delete (string)
    :return: The updated dictionary
    """
    # Vérifier si la clé existe dans le dictionnaire
    if key in a_dictionary:
        # Supprimer la clé du dictionnaire
        del a_dictionary[key]
    return a_dictionary
