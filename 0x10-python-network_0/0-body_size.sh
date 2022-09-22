#!/bin/bash
loop = curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
echo '$1'
