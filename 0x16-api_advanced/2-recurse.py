#!/usr/bin/python3
"""
Reddit's API
"""
import requests

def recurse(subreddit, hot_list=None, after=None):
    """
    Returns top post titles recursively for a given subreddit.
    """
    if hot_list is None:
        hot_list = []

    headers = {'User-Agent': 'api_advanced-project'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'after': after}

    try:
        response = requests.get(url, params=params, headers=headers, allow_redirects=False)
        response.raise_for_status()
        data = response.json()['data']

        for post in data['children']:
            hot_list.append(post['data']['title'])

        if data['after']:
            return recurse(subreddit, hot_list, data['after'])
        else:
            return hot_list

    except (requests.RequestException, KeyError, ValueError):
        return None
