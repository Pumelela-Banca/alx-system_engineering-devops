#!/usr/bin/python3

"""
function that queries the Reddit API
and returns the number of subscribers
(not active users, total subscribers)
for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """
    gets subs from  reddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(
        url, headers={"User-Agent": "My-User-Agent"},
        allow_redirects=False)
    if response.status_code == 200:
        return response.json().get("subscribers")
    else:
        return 0
