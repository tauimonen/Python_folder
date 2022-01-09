"""
Converting space separated list of nine integers to 3 x 3 NumPy array.
"""

import numpy as np
from pip._vendor.distlib.compat import raw_input


def reshape(arr):
    """
    Converting space separated list of nine integers to 3 x 3 NumPy array.
    :param arr: list of integers
    :return: NumPy array
    """
    array = np.array(arr, int)
    return np.reshape(array, (3, 3))


# Take input, use reshape and print the result
input_arr = raw_input().strip().split(' ')
res = reshape(input_arr)
print(res)