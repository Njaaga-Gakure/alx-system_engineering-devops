#!/usr/bin/python3
"""Return number of subscribers."""

import requests


def number_of_subscribers(subreddit):
    """
    Return number of subscribers.

    args:
        subreddit (string): the subreddit

    Returns:
        int: number of subscribers / 0 if invalid

    """
    headers = {
         'User-Agent': 'ApiApp/1.0'
    }
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        no_of_subs = response.json().get('data').get('subscribers')
        return no_of_subs
    elif response.status_code == 404:
        return 0
