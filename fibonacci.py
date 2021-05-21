"""Testing two fast algorithms for fibonacci problem. The first
algorithm seems to be very fast when n is really big. It seems to be
still fast when n = 10 000"""

import time
from functools import lru_cache
fibon_cache = {}

@lru_cache()
def fibonacci(n):
    """Returns n:th fibonacci number. Param: int, return: int"""
    if type(n) != int:
        raise TypeError("n should be positive integer value")
    if n < 1:
        raise ValueError("n should be positive integer value")

    # Returns cached value, if available.
    if n in fibon_cache:
        return fibon_cache[n]

    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)
    fibon_cache[n] = value
    return value


def fib(n: int) -> int:
    a, b = 0, 1
    for i in range(n): a, b = b, a + b
    return a

start = time.time()
for i in range(1, 1001):
    print(i, ":", fib(i))
end = time.time()


start2 = time.time()
for i in range(1, 1001):
    print(i, ":", fibonacci(i))
end2 = time.time()

print(f"Runtime of the fibonacci function is {end2 - start2}")
print(f"Runtime of the fib function is {end - start}")

