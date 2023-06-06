#!/usr/bin/python3
"""Print the titles of the first 10 hot posts."""

import requests


def top_ten(subreddit):
    """
     Print the titles of the first 10 hot posts.

    args:
        subreddit (string): the subreddit
    """
    headers = {
         'User-Agent': 'ApiApp/1.0'
    }
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        posts = response.json().get('data').get('children')
        for post in posts[:10]:
            title = post.get('data').get('title')
            print(title)
    elif response.status_code == 404:
        print(None)
