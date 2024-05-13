#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Création d'une nouvelle matrice vide
    new_matrix = []
    # Itération sur chaque ligne de la matrice originale
    for row in matrix:
        # Utilisation d'une liste en compréhension pour calculer le carré
        squared_row = [x**2 for x in row]
        # Ajout de la ligne calculée à la nouvelle matrice
        new_matrix.append(squared_row)
    return new_matrix
