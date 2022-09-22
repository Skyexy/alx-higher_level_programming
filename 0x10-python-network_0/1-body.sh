#!/bin/bash
# a Bash script that takes in a URL, sends a GET
curl -sI "$1" | grep -i Status
