#!/usr/bin/python3
import urllib.request as r
import urllib.parse as p
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    value = {
        'email': sys.argv[2]
        }

    data = p.urlencode(value)
    data = data.encode('ascii')
    req = r.Request(url, data)
    try:
        with r.urlopen(req) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except Exception as e:
        pass
