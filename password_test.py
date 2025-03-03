import requests
from passwords import GITHUB_USERNAME, GITHUB_TOKEN
# GitHub API URL
api_url = f"https://api.github.com/users/{GITHUB_USERNAME}/repos"

# Send a GET request to the GitHub API with authentication
response = requests.get(api_url, auth=(GITHUB_USERNAME, GITHUB_TOKEN))

# Check if the request was successful
if response.status_code == 200:
    print(f"Authenticated as {GITHUB_USERNAME}")
    repos = response.json()
    print("Repositories:")
    for repo in repos:
        print(f"- {repo['name']}")
else:
    print(f"Failed to authenticate or fetch data. Status Code: {response.status_code}")
