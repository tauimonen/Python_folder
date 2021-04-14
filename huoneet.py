def fill(house, y, x):
    if house[y][x] == "#":
        return
    house[y][x] = "#"
    fill(house, y - 1, x)
    fill(house, y + 1, x)
    fill(house, y, x - 1)
    fill(house, y, x + 1)

def count(r):
    n = len(r)
    m = len(r[0])
    house = [list(r[x]) for x in range(n)]
    result = 0
    for i in range(n):
        for j in range(m):
            if house[i][j] == ".":
                fill(house, i, j)
                result += 1
    return result


if __name__ == "__main__":
    r = ["########",
         "#..#...#",
         "####.#.#",
         "#..#.#.#",
         "########"]
    print(count(r)) # 3