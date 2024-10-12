#!/usr/bin/env python3
""""
A type-annotated function make_multiplier that takes a float multiplier as
argument and returns a function that multiplies a float by multiplier.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    A function that takes a float multiplier and returns a function
    that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that multiplies a
        float by the multiplier.
    """
    def multiplier_function(value: float) -> float:
        """Multiply the given value by the multiplier."""
        return value * multiplier

    return multiplier_function
