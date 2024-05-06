#!/usr/bin/python3
for current_number in range(100):
    # Applique un formatage à deux chiffres avec un remplissage de zéro pour les nombres inférieurs à 10
    if current_number < 99:
        print(f"{current_number:02}, ", end="")
    else:
        # Le dernier nombre est suivi par un saut de ligne
        print(f"{current_number:02}")