#!/usr/bin/python3
"""
script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
Usage: ./10-my_github.py <Github username> <Github password>
    - Uses Basic Authentification to access the ID
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://github.com/user", auth=auth)
    print(r.json().get("id"))
