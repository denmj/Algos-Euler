import numpy as np
import math


def is_power_of_four(n):
    """Find if n is power of four"""
    if n == 0:
        return False
    while n != 1:
        if n % 4 != 0:
            return False
        n = n // 4
    return True

