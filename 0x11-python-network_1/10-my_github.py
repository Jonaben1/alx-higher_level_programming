#!/usr/bin/python3
"""
Write a Python script that takes your GitHub
credentials (username and password) and uses
the GitHub API to display your id
"""
import requests
import sys


if __name__ == '__main__':
    username = sys.argv[1]
    passwd = sys.argv[2]
    req = requests.get("https://api.github.com/user", auth=(username, passwd))
    print(req.json().get('id'))
