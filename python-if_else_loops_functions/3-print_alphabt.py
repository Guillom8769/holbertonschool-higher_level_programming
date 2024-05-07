#!/usr/bin/python3
for ascii_code in range(97, 123):
    letter = chr(ascii_code)
    if letter != 'q' and letter != 'e':
        print(f"{letter}", end="")
