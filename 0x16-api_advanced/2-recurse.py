#!/usr/bin/python3
"""Return a list containing the titles of all hot articles."""


import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """Return a list containing the titles of all hot articles."""
    header = {
              "User-Agent": "ApiApp/1.0"
    }
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    params = {
              "after": after,
              "count": count,
              "limit": 100
    }
    response = requests.get(url, headers=header,
                            params=params, allow_redirects=False)
    if response.status_code == 200:
        data = response.json().get("data")
        after = data.get("after")
        count += data.get("dist")
        for post in data.get("children"):
            hot_list.append(post.get("data").get("title"))
    else:
        return None
    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
