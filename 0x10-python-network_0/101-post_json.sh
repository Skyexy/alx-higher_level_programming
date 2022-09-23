#!/bin/bash
# a Bash script that sends a JSON POST request to a URL
curl -sX POST "$1" -H "Content-Type: application/json" -d @"$2"
