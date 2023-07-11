#!/usr/bin/python3
'''Importing json module
'''
import json


def load_from_json_file(filename):
    '''load_from_json_file - creates an object from a json file
    Args:
        filename: json file to be loaded into memory
    '''
    with open(filename) as file:
        return json.load(file)
