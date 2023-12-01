#!/usr/bin/python3
"""a Python script that takes in a letter and
sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]
    url = 'http://0.0.0.0:5000/search_user'
    value = {'q': q}
    req = requests.post(url, data=value)
    try:
        req_dict = req.json()
        id = req_dict.get('id')
        name = req_dict.get('name')
        if len(req_dict) == 0 or not id or not name:
            print('No result')
        else:
            print(f'[{id}] {name}')
    except requests.exceptions.JSONDecodeError:
        print('Not a valid JSON')
