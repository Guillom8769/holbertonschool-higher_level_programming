#!/usr/bin/python3
def common_elements(set_1, set_2):
    """
    Return a set of common elements in two sets.
    :param set_1: First set of elements
    :param set_2: Second set of elements
    :return: A set containing common elements between `set_1` and `set_2`
    """
    # Utiliser l'intersection des ensembles pour obtenir les éléments communs
    common_set = set_1.intersection(set_2)
    return common_set
