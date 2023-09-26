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
    if len(sys.argv) != 3:
        print("Usage: ./10-my_github.py <Github username> <Github password>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]

    # Construct the API URL to get user information
    url = "https://api.github.com/user"

    # Send a GET request with Basic Authentication
    auth = HTTPBasicAuth(username, password)
    response = requests.get(url, auth=auth)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data.get("id")
        print("Your GitHub user ID is:", user_id)
    else:
        print("Failed to retrieve user data. Please check your credentials")
        sys.exit(1)
