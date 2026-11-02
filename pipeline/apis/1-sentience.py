#!/usr/bin/env python3
"""Module to retrieve the homeworld planets of all sentient species from SWAPI."""
import requests


def sentientPlanets():
    """Returns a list of names of the home planets of all sentient species.

    Handles pagination across all species and resolves homeworld URLs.

    Returns:
        list: Names of the home planets of all sentient species.
    """
    url = "https://swapi-api.alx-tools.com/api/species/"
    planets = []
    planet_cache = {}

    while url:
        response = requests.get(url).json()

        for species in response.get("results", []):
            classification = species.get("classification", "")
            designation = species.get("designation", "")

            # A species is considered sentient if its classification or designation indicates sentience
            if "sentient" in classification.lower() or "sentient" in designation.lower():
                homeworld_url = species.get("homeworld")

                if not homeworld_url:
                    planets.append("unknown")
                else:
                    if homeworld_url in planet_cache:
                        planets.append(planet_cache[homeworld_url])
                    else:
                        homeworld_data = requests.get(homeworld_url).json()
                        planet_name = homeworld_data.get("name", "unknown")
                        planet_cache[homeworld_url] = planet_name
                        planets.append(planet_name)

        url = response.get("next")

    return planets
