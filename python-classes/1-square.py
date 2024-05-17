#!/usr/bin/python3
"""
Module 1-square
Ce module définit une classe Square avec un attribut privé pour
représenter un carré.
"""

class Square:
    """
    Classe Square qui définit un carré avec un attribut privé size.
    """

    def __init__(self, size):
        """
        Initialise un nouveau carré avec une taille spécifiée.
        :param size: Taille du carré
        """
        self.__size = size  # Attribut d'instance privé
