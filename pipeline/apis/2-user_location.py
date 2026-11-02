#!/usr/bin/env python3
"""Script that fetches and prints the location of a specific GitHub user."""
import math
import sys
import time
import requests


def get_user_location():
    """Fetches user location from GitHub API handling errors and rate limits."""
    if len(sys.argv) < 2:
        return

    url = sys.argv[1]
    res = requests.get(url)

    if res.status_code == 200:
        data = res.json()
        print(data.get('location'))
    elif res.status_code == 404:
        print("Not found")
    elif res.status_code == 403:
        reset_time = int(res.headers.get('X-Ratelimit-Reset', 0))
        now = int(time.time())
        diff_minutes = math.ceil((reset_time - now) / 60)
        print("Reset in {} min".format(diff_minutes))


if __name__ == '__main__':
    get_user_location()
