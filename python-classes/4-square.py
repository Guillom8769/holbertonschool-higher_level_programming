#!/usr/bin/python3
"""
Module 4-square
Ce module définit une classe Square avec un attribut privé pour représenter un carré.
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
        self.size = size  # Utilise le setter pour valider et assigner

    @property
    def size(self):
        """
        Getter pour l'attribut privé size.
        :return: La taille du carré
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter pour l'attribut privé size avec vérification de type et de valeur.
        :param value: La nouvelle taille du carré
        :raises TypeError: si value n'est pas un entier
        :raises ValueError: si value est < 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calcule et retourne l'aire du carré.
        :return: Aire du carré
        """
        return self.__size ** 2
