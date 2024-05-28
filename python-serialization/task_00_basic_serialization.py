#!/usr/bin/python3

import json

def serialize_and_save_to_file(data, filename):
    """
    Sérialiser un dictionnaire Python dans un fichier JSON.

    Args:
        data (dict): Un dictionnaire Python contenant les données.
        filename (str): Le nom du fichier de sortie JSON. 
                        Si le fichier de sortie existe déjà, il doit être remplacé.
    """
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """
    Charger et désérialiser un fichier JSON pour recréer un dictionnaire Python.

    Args:
        filename (str): Le nom du fichier d'entrée JSON.

    Returns:
        dict: Un dictionnaire Python avec les données désérialisées du fichier.
    """
    with open(filename, 'r') as file:
        return json.load(file)
