def count(coins):
    total_sum = sum(coins)
    possible = [False] * (total_sum + 1)    # + 1 because of zero
    possible[0] = True
    ways = 0
    for c in coins:
        for i in range(total_sum, -1, -1):
            print(f"coin: {c}, i: {i}, possible: {possible}")
            print(50*"=")
            if possible[i] and not possible[i+c]:
                possible[i+c] = True
                ways += 1
    return ways


if __name__ == "__main__":
    print(count([3,4,5])) # 7
