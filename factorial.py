def fact(n):
    """
    Calculate n! iteratively
    :param n: int
    :return result: int
    """
    result = 1
    if n > 1:
        for f in range(2, n+1):
            result += f
    return result


for i in range(130):
    print(i, fact(i))

