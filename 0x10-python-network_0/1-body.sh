#!/bin/bash
# This script sends a GET request to a URL and displays the body of the response
curl -s "$1" -X GET -D - | awk '/^HTTP/ {if ($2 == 200) {p=1} else {p=0}} p'
