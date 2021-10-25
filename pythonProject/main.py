"""
calc_pi.py: computes the value of Pi using Monte-Carlo Integration
"""

import numpy as np
from numba import jit
import time

n = 2 * 10**8


def timethis(method):
    '''decorator for timing function calls'''
    def timed(*args, **kwargs):
        ts = time.time()
        result = method(*args, **kwargs)
        te = time.time()
        print('{!r} {:f} s'.format(method.__name__, te - ts))
        return result
    return timed


@timethis
def calc_pi(n):
    x = 2 * np.random.ranf(n) - 1
    y = 2 * np.random.ranf(n) - 1
    pi = 4 * np.sum(x**2 + y**2 < 1) / n
    print("result:", pi)
    return pi


@timethis
@jit(nopython=True)
def calc_pi2(n):
    x = 2 * np.random.ranf(n) - 1
    y = 2 * np.random.ranf(n) - 1
    pi = 4 * np.sum(x**2 + y**2 < 1) / n
    print("result:", pi)
    return pi


print("python:")
calc_pi(n)


print("numba:")
calc_pi2(n)

print("numba:")
calc_pi2(n)


