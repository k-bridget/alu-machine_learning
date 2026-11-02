#!/usr/bin/env python3
"""Script that displays the number of launches per rocket using SpaceX API."""
from collections import Counter
import requests


def rocket_frequency():
    """Fetches all launches and counts launches per rocket."""
    launches_url = "https://api.spacexdata.com/v4/launches"
    res = requests.get(launches_url)

    if res.status_code != 200:
        return

    launches = res.json()

    # Count occurrences of each rocket ID
    rocket_counts = Counter(
        launch.get("rocket") for launch in launches if launch.get("rocket")
    )

    # Fetch names for the rocket IDs
    rockets_url = "https://api.spacexdata.com/v4/rockets"
    rockets_res = requests.get(rockets_url)

    if rockets_res.status_code != 200:
        return

    rockets = rockets_res.json()
    rocket_names = {r.get("id"): r.get("name") for r in rockets}

    # Map counts to rocket names
    named_counts = [
        (rocket_names[r_id], count)
        for r_id, count in rocket_counts.items()
        if r_id in rocket_names
    ]

    # Sort descending by count (-x[1]), ascending by name (x[0])
    sorted_rockets = sorted(named_counts, key=lambda x: (-x[1], x[0]))

    for name, count in sorted_rockets:
        print(f"{name}: {count}")


if __name__ == "__main__":
    rocket_frequency()
