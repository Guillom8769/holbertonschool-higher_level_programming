#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Print the first x elements of a list and only integers.
    :param my_list: List of elements
    :param x: Number of elements to access in my_list
    :return: The number of integers printed
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # Ignorer les éléments non formatés comme des entiers
            continue
        except IndexError:
            # Arrêter la boucle si l'indice dépasse la longueur de la liste
            break
    print()  # Imprimer une nouvelle ligne après la boucle
    return count
