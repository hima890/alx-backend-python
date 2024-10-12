#!/usr/bin/env python3
""""
A type-annotated function to_kv that takes a string k and an int OR float v
as arguments and returns a tuple. The first element of the tuple is
the string k.
The second element is the square of the int/float v and should be annotated
as a float.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    A function that takes a string and a number (int or float),
    and returns a tuple. The tuple contains the string and the square of the
    number as a float.

    Args:
        k (str): A string value.
        v (Union[int, float]): A number that can be either an integer
        or a float.

    Returns:
        Tuple[str, float]: A tuple where the first element is the string,
                           and the second element is the square of the number
                           as a float.
    """
    return (k, float(v ** 2))
