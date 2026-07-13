#!/usr/bin/env python3
"""Defines the Binomial distribution class"""


class Binomial:
    """Represents a binomial distribution"""

    def __init__(self, data=None, n=1, p=0.5):
        """
        Class constructor

        data: list of the data to be used to estimate the distribution
        n: number of Bernoulli trials
        p: probability of a success
        """
        if data is None:
            if n <= 0:
                raise ValueError('n must be a positive value')
            if p <= 0 or p >= 1:
                raise ValueError('p must be greater than 0 and less than 1')
            self.n = int(n)
            self.p = float(p)
        else:
            if not isinstance(data, list):
                raise TypeError('data must be a list')
            if len(data) < 2:
                raise ValueError('data must contain multiple values')
            mean = sum(data) / len(data)
            variance = sum((x - mean) ** 2 for x in data) / len(data)
            p = 1 - (variance / mean)
            n = round(mean / p)
            self.n = int(n)
            self.p = float(mean / n)

    def pmf(self, k):
        """
        Calculates the value of the PMF for a given number of successes

        k: number of successes
        """
        k = int(k)
        if k < 0 or k > self.n:
            return 0

        n = self.n
        p = self.p

        def factorial(num):
            result = 1
            for i in range(1, num + 1):
                result *= i
            return result

        n_choose_k = factorial(n) / (factorial(k) * factorial(n - k))
        pmf = n_choose_k * (p ** k) * ((1 - p) ** (n - k))
        return pmf

    def cdf(self, k):
        """
        Calculates the value of the CDF for a given number of successes

        k: number of successes
        """
        k = int(k)
        if k < 0 or k > self.n:
            return 0

        cdf = 0
        for i in range(k + 1):
            cdf += self.pmf(i)
        return cdf
