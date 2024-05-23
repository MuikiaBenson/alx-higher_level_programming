#!/usr/bin/python3
"""takes your GitHub credentials (username and password) and uses the GitHub
API to display your id"""
import requests
from sys import argv


if __name__ == '__main__':
    r = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    try:
        json_response = r.json()
        if 'id' in json_response:
            print(json_response['id'])
        else:
            print('No user ID found in the response')
    except ValueError:
        print('Not a valid JSON')
