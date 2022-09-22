#!/bin/bash
URL = $1
size = curl -I $URL | grep -i Content-Length | awk '{print $2}'
echo size
