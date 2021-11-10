def count(t):
    summa = sum(t)
    ways = 0
    possible = [False] * (summa + 1)
    possible[0] = True

    for coin in t:
        for i in range(summa, -1, -1):
            if possible[i] and not possible[i + coin]:
                possible[i + coin] = True
                ways += 1

    return ways


if __name__ == "__main__":
    print(count([3, 4, 5]))  # 7
    print(count([1, 1, 2]))  # 4
    print(count([2, 2, 2, 3, 3, 3]))  # 13
    print(count([42, 5, 5, 100, 1, 3, 3, 7]))  # 91
