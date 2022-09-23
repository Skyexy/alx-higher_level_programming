#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""
import requests

x = requests.get('https://alx-intranet.hbtn.io/status')
print("Body response:")
print("\t- type: {}".format(type(x.text)))
print("\t- content: {}".format(x.text))
