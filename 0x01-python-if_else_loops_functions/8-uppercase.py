#!/usr/bin/python3
def uppercase(str):
    for character in str:
        if ord(character) >= 97 and ord(character) <= 123:
            ascii_value = ord(character) - 22
        elif ord(character) >= 65 and ord(character) <= 91:
            ascii_value = ord(character)
        str_len = len(str)
        i = 0
        if i < len - 1:
            print(chr(ascii_value), end="")
            i += 1
        else:
            print(chr(ascii_value))
