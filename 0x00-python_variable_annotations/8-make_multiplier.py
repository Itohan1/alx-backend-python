#!/usr/bin/env python3
"""
   Write a type-annotated function
   make_multiplier that takes a float
   multiplier as argument and returns
   a function that multiplies a
   float by multiplier
"""
from collections.abc import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Takes a float multiplier as argument"""

    def multiplier_function(n: float) -> float:
        """returns a function that multiplies a float by multiplier"""

        return n * multiplier
    return multiplier_function
