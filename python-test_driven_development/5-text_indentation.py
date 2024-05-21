#!/usr/bin/python3
"""
Module 5-text_indentation
Ce module fournit une fonction `text_indentation
` pour imprimer un texte avec
2 nouvelles lignes après chaque caractère spécifié.
"""


def text_indentation(text):
    """
    Imprime un texte avec 2 nouvelles lignes après chaque '.', '?' et ':'.

    Args:
        text (str): Le texte à imprimer.

    Raises:
        TypeError: Si le texte n'est pas une chaîne de caractères.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    characters = ['.', '?', ':']
    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in characters:
            result += "\n\n"
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1

    print(result, end='')
