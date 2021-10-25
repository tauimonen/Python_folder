import bodo
import time
import numpy as np


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
@bodo.jit
def calc_pi2(n):
    x = 2 * np.random.ranf(n) - 1
    y = 2 * np.random.ranf(n) - 1
    pi = 4 * np.sum(x**2 + y**2 < 1) / n
    print("result:", pi)
    return pi


if __name__ == "__main__":
    n = 2 * 10 ** 8
    calc_pi2(n)
