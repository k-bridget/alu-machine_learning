#!/usr/bin/env python3
"""Module to retrieve the homeworld planets of sentient species from SWAPI."""
import requests


def sentientPlanets():
    """Returns a list of names of home planets of all sentient species."""
    url = "https://swapi-api.alx-tools.com/api/species/"
    planets = []

    while url:
        res = requests.get(url).json()

        for species in res.get("results", []):
            classification = species.get("classification")
            designation = species.get("designation")

            if classification == "sentient" or designation == "sentient":
                homeworld = species.get("homeworld")
                if homeworld:
                    hw_res = requests.get(homeworld).json()
                    planets.append(hw_res.get("name"))
                else:
                    planets.append("unknown")

        url = res.get("next")

    return planets
