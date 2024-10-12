#!/usr/bin/python3
""" A type-annotated function floor which takes a float n as argument and
returns the floor of the float."""
import math


def floor(n: float) -> int:
    """
    Function Name: floor

    Description:
        Function floor which takes a float n as argument and returns the
        floor of the float

    Args:
        n (float): int input

    Returns:
        float: The floor of the float
    """
    return(math.floor(n))
