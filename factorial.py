def fact(n):
    """
    Calculate n! iteratively
    :param n: int
    :return result: int
    """
    result = 1
    if n > 1:
        for f in range(2, n+1):
            result *= f
    return result


def factorial(n):
    """
    Calculate n! recursively
    :param n: int
    :return: int
    """
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


for i in range(130):
    print(i, factorial(i))

