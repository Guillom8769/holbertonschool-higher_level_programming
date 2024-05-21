# Python Test-Driven Development

## 0. Integers Addition

This project contains a function that adds two integers.

### Function Prototype

```python
def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the sum as an integer.

    Args:
        a (int, float): The first number to add.
        b (int, float): The second number to add. Defaults to 98.

    Returns:
        int: The sum of `a` and `b` after converting them to integers.

    Raises:
        TypeError: If `a` or `b` are not integers or floats.
    """
    
# Python Test-Driven Development

## 2. Matrix Division

Ce projet contient une fonction qui divise tous les éléments d'une matrice par un diviseur.

### Prototype de la Fonction

```python
def matrix_divided(matrix, div):
    """
    Divise tous les éléments d'une matrice par un diviseur et retourne une nouvelle matrice.
    
    Args:
        matrix (list of lists of int/float): La matrice à diviser.
        div (int/float): Le diviseur.

    Returns:
        list of lists of float: Une nouvelle matrice avec les éléments divisés par div, arrondis à 2 décimales.

    Raises:
        TypeError: Si la matrice n'est pas une liste de listes d'entiers ou de flottants,
                   ou si les lignes de la matrice n'ont pas la même taille,
                   ou si le diviseur n'est pas un nombre.
        ZeroDivisionError: Si le diviseur est égal à 0.
    """
