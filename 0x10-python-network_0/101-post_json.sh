#!/bin/bash
# a Bash script that sends a JSON POST request to a URL
curl -sX POST "$1" -d @"$2"
