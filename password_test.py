import os
import requests

# Fetch username and password from environment variables
username = os.getenv('MY_USERNAME')
password = os.getenv('MY_PASSWORD')

# Check if the environment variables are set
if username and password:
    url = "http://host.docker.internal:8000/basic-auth/russ/test"
    response = requests.get(url, auth=(username, password))

    # Print the response
    print(f"Status Code: {response.status_code}")
    print("Response Content:", response.content.decode())
else:
    print("Environment variables MY_USERNAME and MY_PASSWORD are not set.")
