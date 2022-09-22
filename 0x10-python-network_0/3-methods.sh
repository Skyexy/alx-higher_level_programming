#!/bin/bash
# a Bash script that takes in a URL
curl -sI "$1" | grep -i Allow | awk '{ for (i=3; i<=NF; i++) printf("%s ",$i) }END{ print"" }'
