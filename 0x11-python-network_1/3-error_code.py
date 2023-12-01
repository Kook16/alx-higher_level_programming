#!/usr/bin/python3
"""
Script that takes in a URL, send a request to URL, and dispaly body
"""
import urllib.request as r
from urllib.error import HTTPError
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    req = r.Request(url)

    try:
        with r.urlopen(req) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except HTTPError as e:
        print('Error code: ', e.code)
