#!/usr/bin/python3
def pow(a, b):
    result = 1
    if b > 0:
        i = 0
        while i < b:
            result *= a
            i += 1
    elif b < 0:
        i = 0
        x = b * -1
        while i < x:
            result /= a
            i += 1
            if a < 0 ad b % 2 == 1:
                result = -result
    return result
