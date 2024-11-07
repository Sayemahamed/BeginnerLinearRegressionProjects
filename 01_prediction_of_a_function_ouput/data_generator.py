"""
This file contains a function that takes an integer input and returns the result of multiplying it by 2 and adding 47.
"""

import numpy as np


def func(x: int) -> int:
    """
    Takes an integer input and returns the result of multiplying it by 2 and adding 47.

    Parameters:
    x (int): The input integer.

    Returns:
    int: The calculated result.
    """
    return x * 2 + 47


x = np.array([x for x in range(100000)])
y = np.array([func(x.item()) for x in x])
np.savez(file="data",input=x,output=y)