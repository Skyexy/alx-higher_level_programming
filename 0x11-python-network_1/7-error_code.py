#!/usr/bin/python3
"""fetches https://intranet.hbtn.io/status"""
import requests
import sys

if __name__ == "__main__":
    x = requests.get(sys.argv[1])
    try:
        x.raise_for_status()
        print(x.text)
    except Exception as e:
        print("Error code: {}".format(x.status_code))
