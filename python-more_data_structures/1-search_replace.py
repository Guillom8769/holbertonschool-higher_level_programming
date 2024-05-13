#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replace all occurrences of `search` with `replace` in a new list.
    :param my_list: List of elements
    :param search: The element to be replaced
    :param replace: The new element that will replace the `search` element
    :return: A new list with the replacements
    """
    # Création d'une nouvelle liste pour stocker les résultats
    new_list = []
    # Itération sur chaque élément de la liste originale
    for item in my_list:
        if item == search:
            # Si l'élément correspond à `search`, ajouter `replace`
            new_list.append(replace)
        else:
            # Sinon, ajouter l'élément actuel
            new_list.append(item)
    return new_list
