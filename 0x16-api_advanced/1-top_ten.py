#!/usr/bin/python3

"""
prints the titles of the first 10 hot posts listed for a given subreddit.
"""

import requests

def top_ten(subreddit):
    """
    Prints the titles of the top 10 hot posts for a given subreddit.
    If the subreddit is invalid or an error occurs, prints "None".
    """
    if not isinstance(subreddit, str):
        print("None")
        return

    url = f'https://www.reddit.com/r/{subreddit}/hot/.json'
    headers = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    params = {'limit': 10}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        for post in data['data']['children']:
            print(post['data']['title'])
    except (requests.RequestException, KeyError, ValueError):
        print("None")
