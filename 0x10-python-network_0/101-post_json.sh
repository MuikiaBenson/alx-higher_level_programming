#!/bin/bash
# sends a POST request with the contents of a JSON file passed as the second argument to the URL passed as the first argument
curl -s -X POST -d @"$2" -H "Content-Type: application/json" "$1"
