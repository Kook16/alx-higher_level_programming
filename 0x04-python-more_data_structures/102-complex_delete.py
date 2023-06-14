#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary is None:
        return
    if value not in a_dictionary.values():
        return a_dictionary
    a_dic_copy = a_dictionary.copy()
    for key, item in a_dic_copy.items():
        if value == item:
            a_dictionary.pop(key)
    return a_dictionary
