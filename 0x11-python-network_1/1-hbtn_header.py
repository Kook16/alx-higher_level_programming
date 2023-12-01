#!/usr/bin/python3
import urllib.request as r
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    req = r.Request(url)

    try:
        with r.urlopen(req) as response:
            header = response.getheaders()
            header_dict = dict(header)
            if 'X-Request-Id' in header_dict:
                print(header_dict['X-Request-Id'])
    except Exception as e:
        pass
