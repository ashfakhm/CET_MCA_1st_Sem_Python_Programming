"""Area and circumference calculations for a circle."""

import math

__all__ = ["area", "perimeter"]


def area(radius):
    return math.pi * radius**2


def perimeter(radius):
    return 2 * math.pi * radius
