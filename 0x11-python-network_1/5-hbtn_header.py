#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""
import requests
import sys

x = requests.get(sys.argv[1])
print(x.headers['X-Request-Id'])
