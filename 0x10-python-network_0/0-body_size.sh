#!/bin/bash
#sends a request to URL using curl,and displays the size of the of the response body in bytes.
curl -so /dev/null -w '%{size_download}\n' $1
