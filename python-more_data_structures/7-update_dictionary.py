#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Update or add a key/value pair in the dictionary `a_dictionary`.
    If the key exists, its value will be updated. If it does not exist,
    a new key/value pair will be added.
    :param a_dictionary: Dictionary to be updated
    :param key: Key to update or add (string)
    :param value: Value associated with the key
    """
    # Mettre à jour ou ajouter la clé avec la valeur spécifiée
    a_dictionary[key] = value
    return a_dictionary
