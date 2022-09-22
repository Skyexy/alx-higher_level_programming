#!/bin/bash
# a Bash script that takes in a URL
curl -sI "$1" | grep -i Allow | awk '{print $2}'
