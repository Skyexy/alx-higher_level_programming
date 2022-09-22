#!/bin/bash
URL = "HTTP://$1"
size = curl -sI $URL | grep -i Content-Length | awk '{print $2}'
echo size
