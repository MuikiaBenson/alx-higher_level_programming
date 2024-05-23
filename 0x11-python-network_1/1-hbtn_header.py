#!/usr/bin/python3
"""Fetches the X-Request-Id header from a URL response"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    with urllib.request.urlopen(request) as response:
        headers = response.getheaders()
        for header in headers:
            if header[0] == "X-Request-Id":
                print(header[1])
                break
