def count(n, start=1):
    if n == 0:
        return 1
    ways = 0
    for i in range(start, n+1):
        print(ways)
        ways += count(n-i, i)
    return ways


if __name__ == "__main__":
    print(count(4)) # 5
