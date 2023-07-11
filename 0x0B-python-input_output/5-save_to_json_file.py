#!/usr/bin/python3
'''Defining save_to_json_file function
'''
import json


def save_to_json_file(my_obj, filename):
    '''save_to_json_file - writes an object to a text file using json
    representation
    Args:
        my_obj: object to be written to a text file
        filename: file which is gonna be written to
    '''
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
