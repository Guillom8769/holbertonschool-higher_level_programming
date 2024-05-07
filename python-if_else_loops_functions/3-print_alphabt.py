#!/usr/bin/python3
for code in range(97, 123):
    letter = chr(code)
    if letter != 'q' and letter != 'e':
        print(f"{letter}", end="")
