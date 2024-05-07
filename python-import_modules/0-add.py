#!/usr/bin/python3

# Importer la fonction add depuis le fichier add_0
from add_0 import add

# Définir les variables a et b
a = 1
b = 2

# Calculer le résultat en appelant la fonction add
result = add(a, b)

# Afficher le résultat avec `format`
print("{} + {} = {}".format(a, b, result))
