#!/usr/bin/python3

if __name__ == "__main__":
    # Importer les fonctions depuis calculator_1
    from calculator_1 import add, sub, mul, div

    # Définir les variables a et b
    a = 10
    b = 5

    # Effectuer et afficher les opérations
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
