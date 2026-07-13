#!/usr/bin/env python3
"""Defines the Normal distribution class"""


class Normal:
    """Represents a normal distribution"""

    def __init__(self, data=None, mean=0., stddev=1.):
        """
        Class constructor

        data: list of the data to be used to estimate the distribution
        mean: mean of the distribution
        stddev: standard deviation of the distribution
        """
        if data is None:
            if stddev <= 0:
                raise ValueError('stddev must be a positive value')
            self.mean = float(mean)
            self.stddev = float(stddev)
        else:
            if not isinstance(data, list):
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            self.mean = float(sum(data) / len(data))
            variance = sum((x - self.mean) ** 2 for x in data) / len(data)
            self.stddev = variance ** 0.5

    def z_score(self, x):
        """
        Calculates the z-score of a given x-value

        x: the x-value
        """
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """
        Calculates the x-value of a given z-score

        z: the z-score
        """
        return z * self.stddev + self.mean

    def pdf(self, x):
        """
        Calculates the value of the PDF for a given x-value

        x: the x-value
        """
        e = 2.7182818285
        pi = 3.1415926536
        mean = self.mean
        stddev = self.stddev

        coefficient = 1 / (stddev * ((2 * pi) ** 0.5))
        exponent = -((x - mean) ** 2) / (2 * (stddev ** 2))
        pdf = coefficient * (e ** exponent)
        return pdf

    def cdf(self, x):
        """
        Calculates the value of the CDF for a given x-value

        x: the x-value
        """
        pi = 3.1415926536
        mean = self.mean
        stddev = self.stddev

        arg = (x - mean) / (stddev * (2 ** 0.5))
        erf = (2 / (pi ** 0.5)) * (
            arg
            - (arg ** 3) / 3
            + (arg ** 5) / 10
            - (arg ** 7) / 42
            + (arg ** 9) / 216
        )
        cdf = 0.5 * (1 + erf)
        return cdf
