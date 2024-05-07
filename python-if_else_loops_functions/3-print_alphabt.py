#!/usr/bin/python3
for code in range(97, 123):
    letter = chr(code)
    if letter != 101 and letter != 113:
        print(f"{letter}", end="")
