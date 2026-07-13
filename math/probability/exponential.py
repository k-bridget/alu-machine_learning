#!/usr/bin/env python3
"""Defines the Exponential distribution class"""


class Exponential:
    """Represents an exponential distribution"""

    def __init__(self, data=None, lambtha=1.):
        """
        Class constructor

        data: list of the data to be used to estimate the distribution
        lambtha: expected number of occurences in a given time frame
        """
        if data is None:
            if lambtha <= 0:
                raise ValueError('lambtha must be a positive value')
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            self.lambtha = float(len(data) / sum(data))

    def pdf(self, x):
        """
        Calculates the value of the PDF for a given time period

        x: time period
        """
        if x < 0:
            return 0

        e = 2.7182818285
        lambtha = self.lambtha

        pdf = lambtha * (e ** (-lambtha * x))
        return pdf

    def cdf(self, x):
        """
        Calculates the value of the CDF for a given time period

        x: time period
        """
        if x < 0:
            return 0

        e = 2.7182818285
        lambtha = self.lambtha

        cdf = 1 - (e ** (-lambtha * x))
        return cdf
