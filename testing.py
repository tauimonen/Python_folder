def count(r):
    n = len(r)
    m = len(r[0])
    count = [[0]*m for _ in range(n)]
    inf = 10**9

    for i in range(n):
        for j in range(m):
            if r[i][j] == "A":
                si = i
                sj = j
            if r[i][j] == "B":
                ei = i
                ej = j

    print(si, sj, ei, ej)
    for i in range(n):
        for j in range(m):
            count[i][j] = inf
            if r[i][j] == "#":
                continue
            if i == 0 and j == 0:
                count[si][sj] = 0
            if i-1 >= 0:
                count[i][j] = min(count[i][j],count[i-1][j])
            if j-1 >= 0:
                count[i][j] = min(count[i][j],count[i][j-1])
            if r[i][j] == "*":
                count[i][j] += 1
    print(count)
    return -1 if count[ei][ej] == inf else count[ei][ej]


if __name__ == "__main__":
    r = ["########",
         "#*A*...#",
         "#.*****#",
         "#.**.**#",
         "#.*****#",
         "#..*.B.#",
         "########"]
    print(count(r))


