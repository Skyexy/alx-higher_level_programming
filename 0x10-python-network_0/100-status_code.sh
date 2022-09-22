#!/bin/bash
# a Bash script that takes in a URL, sends a GET
curl -s -o /dev/null -I --w '%{http_code}' "$1"
