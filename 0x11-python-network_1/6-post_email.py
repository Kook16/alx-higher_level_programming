#!/usr/bin/python3
import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    email = sys.argv[2]
    value = {
        'email': email
        }

    r = requests.post(url, data=value)

    print(r.text)
