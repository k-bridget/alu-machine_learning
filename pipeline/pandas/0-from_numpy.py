#!/usr/bin/env python3
"""Module that converts a NumPy ndarray into a Pandas DataFrame."""
import pandas as pd


def from_numpy(array):
    """Creates a pd.DataFrame from a np.ndarray.

    Parameters:
        array (np.ndarray): The NumPy array to convert.

    Returns:
        pd.DataFrame: DataFrame with uppercase alphabetical column labels.
    """
    num_cols = array.shape[1]
    columns = [chr(ord('A') + i) for i in range(num_cols)]
    return pd.DataFrame(data=array, columns=columns)
