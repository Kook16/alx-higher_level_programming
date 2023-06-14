#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_integer = float('-inf')
    key_value = None
    for key in a_dictionary.keys():
        if a_dictionary[key] > max_integer:
            max_integer = a_dictionary[key]
            key_value = key
    return key_value
