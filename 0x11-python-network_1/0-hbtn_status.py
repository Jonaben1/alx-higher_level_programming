#!/usr/bin/python3
"""
A Python script that fetches data from a url
"""
import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
    print("Body response:")
    print("\t- type:", type(fetched))
    print("\t- content:", fetched)
    print("\t- utf8 content:", fetched.decode('utf-8'))
