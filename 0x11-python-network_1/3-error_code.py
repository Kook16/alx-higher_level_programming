#!/usr/bin/python3
import urllib.request as r
from urllib.error import URLError
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    req = r.Request(url)

    try:
        with r.urlopen(req) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except URLError as e:
        if hasattr(e, 'code'):
            print('Error code: ', e.code)
