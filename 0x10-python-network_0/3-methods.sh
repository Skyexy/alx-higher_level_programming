#!/bin/bash
# a Bash script that takes in a URL
curl -sI "$1" | grep -i Allow | cut -d " " -f2-
