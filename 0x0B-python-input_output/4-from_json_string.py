#!/usr/bin/python3
'''Defining the from_json_string
'''
import json


def from_json_string(my_str):
    '''from_json_string - converts a json string to a python data structure
    Args:
        my_str: A json string representation
    '''
    return json.loads(my_str)
