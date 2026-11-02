#!/usr/bin/env python3
"""Module for fetching Star Wars starships based on passenger capacity."""
import requests


def availableShips(passengerCount):
    """Returns a list of ships that can hold at least passengerCount passengers.

    Args:
        passengerCount (int): Minimum number of passengers the ship must hold.

    Returns:
        list: List of ship names meeting the criteria, or an empty list.
    """
    url = "https://swapi-api.alx-tools.com/api/starships/"
    ships = []

    while url:
        response = requests.get(url).json()

        for ship in response.get("results", []):
            capacity = ship.get("passengers", "").replace(",", "")
            try:
                if int(capacity) >= passengerCount:
                    ships.append(ship.get("name"))
            except ValueError:
                continue

        url = response.get("next")

    return ships
