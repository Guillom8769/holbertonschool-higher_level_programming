#!/usr/bin/python3

"""
Module pour générer le triangle de Pascal.
"""


def pascal_triangle(n):
    """
    Génère le triangle de Pascal de taille n.
    Args:
        n (int): Le nombre de lignes du triangle.
    Returns:
        list: Une liste de listes représentant le triangle de Pascal.
    """
    if n <= 0:
        return []

    # Initialisation du triangle avec la première ligne
    triangle = [[1]]

    # Générer chaque ligne du triangle
    for i in range(1, n):
        # Commencer chaque ligne avec 1
        row = [1]
        # Remplir les éléments intermédiaires
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        # Terminer chaque ligne avec 1
        row.append(1)
        # Ajouter la ligne au triangle
        triangle.append(row)

    return triangle


# Exemple d'utilisation et de test
if __name__ == "__main__":
    def print_triangle(triangle):
        """
        Affiche le triangle.
        """
        for row in triangle:
            print("[{}]".format(",".join([str(x) for x in row])))

    print_triangle(pascal_triangle(5))
