#!/usr/bin/env python3
"""
a function def poly_derivative(poly):
that calculates the derivative of a polynomial
"""


def poly_derivative(poly):
    """
    calculates the derivative of a polynomial
    """

    if not isinstance(poly, list) or len(poly) == 0:
        return None

    if not all(isinstance(x, (int, float)) for x in poly):
        return None

    if len(poly) == 1:
        return [0]

    derivative = [poly[i] * i for i in range(1, len(poly))]
    return derivative
