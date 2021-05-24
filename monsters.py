def count(r):
    """Calculates minimum count of monster to every square.
    param: list of lists
    returns: int """
    n = len(r)  # row count
    m = len(r[0])   # row length
    count = [[0] * m for _ in range(n)]
    inf = 10**9
    for i in range(n):
        for j in range(m):
            count[i][j] = inf
            if r[i][j] == "#":
                continue
            if i == 0 and j == 0:
                count[i][j] = 0
            if i-1 >= 0:
                count[i][j] = min(count[i][j], count[i-1][j])
            if j-1 >= 0:
                count[i][j] = min(count[i][j], count[i][j-1])
            if r[i][j] == "@":
                count[i][j] += 1

    return -1 if count[n-1][m-1] >= inf else count[n-1][m-1]


if __name__ == "__main__":
    r = ["....@",
         "@##.#",
         ".##@#",
         ".@..#",
         "###@."]
    print(count(r)) # 2