#!/usr/bin/python3

"""Printing the first 10 hot posts in a rededit
"""

from requests import get


def top_ten(subreddit):
    """ The method that prints the post"""

    if subreddit is None or not isinstance(subreddit, str):
        return print("None")

    url = 'http://www.reddit.com/r/{0}/hot/.json'.format(subreddit)
    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    try:
        res = get(url, user_agent)
        json = res.json()
        for i in range(10):
            print(json.get('data').get('children')[i].get("data").get("title"))
    except Exception:
        print("None")
