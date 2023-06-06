#!/usr/bin/python3
def uppercase(str):
    converted_str = ""
    for character in str:
        if ord(character) >= 97 and ord(character) <= 122:
            ascii_value = ord(character) - 32
        else:
            ascii_value = ord(character)
        converted_str += chr(ascii_value)
    print(converted_str)
