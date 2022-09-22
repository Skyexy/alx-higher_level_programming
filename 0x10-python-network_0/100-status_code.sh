#!/bin/bash
# a Bash script that takes in a URL, sends a GET
curl -sw '%{http_code}' "$1"
