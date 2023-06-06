#!/usr/bin/python3
def pow(a, b):
    result = 1
    i = 0
    while i < b:
        result *= a
        i += 1
    return result
