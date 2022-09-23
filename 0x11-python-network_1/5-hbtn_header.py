#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""
import requests
import sys

if __name__ == "__main__":
    x = requests.get(sys.argv[1])
    print(x.headers.get('X-Request-Id'))
