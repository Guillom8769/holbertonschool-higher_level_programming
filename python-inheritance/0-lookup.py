#!/usr/bin/python3
def lookup(obj):
    """
    Retourne la liste des attributs et méthodes disponibles pour un objet donné.

    Args:
        obj: L'objet dont on veut lister les attributs et méthodes.

    Returns:
        Une liste des noms des attributs et méthodes disponibles de l'objet.
    """
    # Utilise la fonction intégrée `dir` pour obtenir la liste des attributs et méthodes
    return dir(obj)
