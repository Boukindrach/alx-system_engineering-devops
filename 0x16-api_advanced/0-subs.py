#!/usr/bin/python3

"""gives number of subscribers"""
import requests

def number_of_subscribers(subreddit):
    url = "https://www.reddit.com/r/{subreddit}/about.json".format(subreddit)
    headers = {
        "User-Agent": "Custom User Agent 1.0"
    }

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0

    except Exception as e:
        return 0
