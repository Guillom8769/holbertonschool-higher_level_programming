#!/usr/bin/python3
if __name__ == "__main__":  # if the script is executed, not imported

    # Importer uniquement la fonction add depuis add_0
    from add_0 import add

    # Définir les variables
    a = 1
    b = 2

    # Appeler la fonction `add` et récupérer le résultat
    result = add(a, b)

    # Imprimer le résultat en utilisant la méthode `format`
    print("{} + {} = {}".format(a, b, result))
