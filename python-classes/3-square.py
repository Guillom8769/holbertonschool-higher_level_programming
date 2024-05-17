#!/usr/bin/python3
"""
Module 3-square
Ce module définit une classe Square avec un attribut
privé pour représenter un carré.
"""

class Square:
    """
    Classe Square qui définit un carré avec un attribut privé size.
    """

    def __init__(self, size=0):
        """
        Initialise un nouveau carré avec une taille spécifiée.
        :param size: Taille du carré (doit être un entier >= 0)
        :raises TypeError: si size n'est pas un entier
        :raises ValueError: si size est < 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size  # Attribut d'instance privé

    def area(self):
        """
        Calcule et retourne l'aire du carré.
        :return: Aire du carré
        """
        return self.__size ** 2
