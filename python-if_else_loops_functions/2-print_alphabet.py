#!/usr/bin/python3
# Nom de la variable qui explique sa fonction
ascii_code_of_a = 97  # ASCII code for 'a'
ascii_code_of_z = 123  # ASCII code for 'z' + 1 to include 'z' in the range

for ascii_code in range(ascii_code_of_a, ascii_code_of_z):
    print(chr(ascii_code), end='')
