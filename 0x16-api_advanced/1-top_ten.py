#!/usr/bin/python3
"""
function that queries the Reddit API
and prints the titles of the first
10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """
    prints  subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(
        url, headers={"User-Agent": "My-User-Agent"},
        allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get("data")
        for chld in data.get("children")[:10]:
            print(chld.get("data").get("title"))
    else:
        print("None")
