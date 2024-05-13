#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds two tuples element-wise, with each tuple
    containing up to two integers.
    Args:
        tuple_a (tuple): The first tuple to add.
        tuple_b (tuple): The second tuple to add.
    Returns:
        tuple: A tuple containing two integers,
        resulting from the element-wise addition of tuple_a and tuple_b.
    """
    # Compléter les tuples à deux éléments avec des zéros si nécessaire
    if len(tuple_a) < 2:
        tuple_a += (0,) * (2 - len(tuple_a))
    if len(tuple_b) < 2:
        tuple_b += (0,) * (2 - len(tuple_b))
    # Calculer la somme des deux premiers éléments
    result = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return result
