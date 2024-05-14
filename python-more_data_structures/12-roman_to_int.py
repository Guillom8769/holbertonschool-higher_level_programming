#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    Convert a Roman numeral to an integer.
    :param roman_string: String representing the Roman numeral
    :return: The integer value of the Roman numeral
    """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    # Dictionnaire des valeurs des chiffres romains
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    prev_value = 0
    # Parcourir la chaîne de droite à gauche
    for char in reversed(roman_string):
        value = roman_values.get(char, 0)
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    return total
