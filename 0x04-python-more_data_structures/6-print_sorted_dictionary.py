#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        return
    ordered_dic = sorted(a_dictionary.keys())
    for key in ordered_dic:
        print(f'{key}: {a_dictionary[key]}')
