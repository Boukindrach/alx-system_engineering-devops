#!/usr/bin/python3
"""Reddit API word counting function"""

#!/usr/bin/python3

import requests
from collections import Counter
after=""
word_counts=None

def count_words(subreddit, word_list):
    """Count occurrences of words in hot post titles of a subreddit"""
    if word_counts is None:
        word_counts = Counter()

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'user-agent': 'word_counter_bot'}
    params = {'after': after}

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        response.raise_for_status()
        data = response.json()['data']

        for post in data['children']:
            title_words = post['data']['title'].lower().split()
            word_counts.update(word for word in title_words if word.lower() in map(str.lower, word_list))

        if data['after']:
            return count_words(subreddit, word_list, data['after'], word_counts)
        else:
            merged_counts = Counter()
            for word in word_list:
                merged_counts[word.lower()] += word_counts[word.lower()]

            for word, count in sorted(merged_counts.items(), key=lambda x: (-x[1], x[0])):
                if count > 0:
                    print(f"{word}: {count}")

    except requests.RequestException:
        print(f"Error: Unable to fetch data for subreddit '{subreddit}'")
