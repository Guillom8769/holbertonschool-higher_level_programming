#!/usr/bin/python3
"""
Module 9-rectangle
Ce module fournit une classe `Rectangle` qui définit un rectangle
avec des attributs privés pour la largeur et la hauteur,
ainsi que des méthodes pour calculer l'aire, le périmètre et des
représentations sous forme de chaîne de caractères.
"""


class Rectangle:
    """
    Classe qui définit un rectangle par :
    - des attributs privés pour la largeur (width) et la hauteur (height)
    - des propriétés pour accéder et modifier ces attributs avec
      des vérifications
    - des méthodes pour calculer l'aire (area), le périmètre (perimeter)
    - des méthodes pour afficher le rectangle en utilisant `print()`,
      `str()` et `repr()`
    - une méthode pour afficher un message lors de la suppression de l'objet
    - des attributs de classe pour suivre le nombre d'instances et
      personnaliser le symbole de représentation
    - une méthode statique pour comparer deux rectangles
    - une méthode de classe pour créer un carré
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialisation des attributs width et height, et incrémente
        number_of_instances
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Récupère la largeur du rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Définit la largeur du rectangle
        Vérifie que la valeur est un entier et qu'elle est positive
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Récupère la hauteur du rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Définit la hauteur du rectangle
        Vérifie que la valeur est un entier et qu'elle est positive
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Retourne l'aire du rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Retourne le périmètre du rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Retourne une chaîne de caractères représentant le rectangle
        avec le caractère(s) défini dans print_symbol
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rect_lines = [
            str(self.print_symbol) * self.__width for _ in range(self.__height)
        ]
        return "\n".join(rect_lines)

    def __repr__(self):
        """
        Retourne une chaîne de caractères représentant l'objet Rectangle
        Permet de recréer l'objet en utilisant eval()
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Affiche un message lors de la suppression de l'objet Rectangle
        et décrémente number_of_instances
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Retourne le plus grand rectangle basé sur l'aire
        rect_1 et rect_2 doivent être des instances de Rectangle,
        sinon lève une TypeError
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Retourne une nouvelle instance de Rectangle avec largeur == hauteur == size
        """
        return cls(size, size)
