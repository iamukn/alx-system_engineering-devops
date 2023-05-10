#!/usr/bin/python3
from requests import get

"""Making a get request to the Reddit APi and
printing the total subscriber to the console"""


def number_of_subscribers(subreddit):
    """receives a subreddit and returns the total
    subscribers on reddit"""

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}

    res = get(url, headers=user_agent)

    data = res.json()
    try:
        return data.get('data').get('subscribers')
    except Exception:
        return 0


number_of_subscribers('programming')
