#!/usr/bin/env python3
"""Script that fetches and displays the next upcoming SpaceX launch."""
import requests


def get_upcoming_launch():
    """Retrieves and prints details of the soonest upcoming SpaceX launch."""
    url = "https://api.spacexdata.com/v4/launches/upcoming"
    res = requests.get(url)

    if res.status_code != 200:
        return

    launches = res.json()
    if not launches:
        return

    # Sort stably by date_unix; preserves original order on equal timestamps
    sorted_launches = sorted(launches, key=lambda x: x.get("date_unix", 0))
    launch = sorted_launches[0]

    launch_name = launch.get("name")
    date_local = launch.get("date_local")

    # Fetch rocket information
    rocket_id = launch.get("rocket")
    rocket_url = f"https://api.spacexdata.com/v4/rockets/{rocket_id}"
    rocket_res = requests.get(rocket_url).json()
    rocket_name = rocket_res.get("name")

    # Fetch launchpad information
    launchpad_id = launch.get("launchpad")
    launchpad_url = f"https://api.spacexdata.com/v4/launchpads/{launchpad_id}"
    launchpad_res = requests.get(launchpad_url).json()
    launchpad_name = launchpad_res.get("name")
    launchpad_locality = launchpad_res.get("locality")

    # Format: <launch name> (<date>) <rocket name> - <launchpad name> (<locality>)
    print(
        f"{launch_name} ({date_local}) {rocket_name} - "
        f"{launchpad_name} ({launchpad_locality})"
    )


if __name__ == "__main__":
    get_upcoming_launch()
