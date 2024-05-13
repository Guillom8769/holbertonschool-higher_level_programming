#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    Return a set of all elements that are only in one of the two sets.
    :param set_1: First set of elements
    :param set_2: Second set of elements
    :return: A set containing elements that are only in `set_1` or `set_2`
    """
    # l'opérateur de différence symétrique pour obtenir les éléments uniques
    unique_set = set_1.symmetric_difference(set_2)
    return unique_set
