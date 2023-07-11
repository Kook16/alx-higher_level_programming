#!/usr/bin/python3
'''Defining to_JSON_string function
'''
import json


def to_json_string(my_obj):
    '''This function returns the JSON representation of a string
    Args:
         obj: string whose JSON representation is required
    '''
    return json.dumps(my_obj)
