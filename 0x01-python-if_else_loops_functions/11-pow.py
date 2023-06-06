#!/usr/bin/python3
def pow(a, b):
    result = 1
    if b > 0:
        for i in range(b):
            result *= a
    elif b < 0:
        for i in range(-b):
            result /= a
            if a < 0 and b % 2 == 1:
                result = -result
            else:
                result = 1
    return result
