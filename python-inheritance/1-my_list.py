#!/usr/bin/python3
class MyList(list):
    """
    Classe qui hérite de la classe list et ajoute une méthode pour
    imprimer la liste triée.

    Méthodes:
        print_sorted(self): Imprime la liste triée en ordre croissant.
    """
    def print_sorted(self):
        """
        Imprime la liste triée en ordre croissant.

        La méthode utilise la fonction sorted() pour trier la liste
        sans modifier la liste originale.
        """
        print(sorted(self))
