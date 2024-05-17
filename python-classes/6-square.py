#!/usr/bin/python3
"""
Module 6-square
Ce module définit une classe Square avec des attributs privés pour représenter un carré.
"""

class Square:
    """
    Classe Square qui définit un carré avec des attributs privés size et position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialise un nouveau carré avec une taille et une position spécifiées.
        :param size: Taille du carré (doit être un entier >= 0)
        :param position: Position du carré (doit être un tuple de 2 entiers positifs)
        :raises TypeError: si size n'est pas un entier ou si position n'est pas un tuple de 2 entiers positifs
        :raises ValueError: si size est < 0 ou si un des éléments de position est < 0
        """
        self.size = size  # Utilise le setter pour valider et assigner
        self.position = position  # Utilise le setter pour valider et assigner

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

    @property
    def position(self):
        """
        Getter pour l'attribut privé position.
        :return: La position du carré
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter pour l'attribut privé position avec vérification de type et de valeur.
        :param value: La nouvelle position du carré
        :raises TypeError: si value n'est pas un tuple de 2 entiers positifs
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calcule et retourne l'aire du carré.
        :return: Aire du carré
        """
        return self.__size ** 2

    def my_print(self):
        """
        Affiche le carré avec le caractère # dans stdout en utilisant position pour l'alignement.
        Si la taille est 0, imprime une ligne vide.
        """
        if self.__size == 0:
            print("")
            return

        # Imprime les lignes vides en fonction de position[1]
        for _ in range(self.__position[1]):
            print("")

        # Imprime les lignes du carré avec les espaces de décalage en fonction de position[0]
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
