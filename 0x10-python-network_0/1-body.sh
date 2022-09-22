#!/bin/bash
# a Bash script that takes in a URL, sends a GET
curl -sfL "$1" -X GET
