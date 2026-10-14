#!/usr/bin/env python3
"""Module that loads data from a delimited file into a Pandas DataFrame."""
import pandas as pd


def from_file(filename, delimiter):
    return pd.read_csv(filename, sep=delimiter)

