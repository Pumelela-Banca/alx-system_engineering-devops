#!/usr/bin/python3
"""
recursive function that queries the
Reddit API and returns a list containing the
titles of all hot articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    recursive function that queries the
    Reddit API and returns a list containing the
    titles
    """
    response = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "Custom"},
        params={"after": after},
        allow_redirects=False
    )
    if response.status_code == 200:
        data = response.json().get("data")
        for chld in data.get("children"):
            hot_list.append(chld.get("data").get("title"))
        after = data.get("after")
        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
