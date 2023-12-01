#!/usr/bin/python3
"""
Script that takes in a URL and an email address,
sends a POST request to the passed URL
with the email as a parameter, an
finally displays the body of the response
"""

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    req = requests.get(url)
    status_code = req.status_code
    if status_code < 400:
        print(req.text)
    else:
        print(f'Error code: {status_code}')
