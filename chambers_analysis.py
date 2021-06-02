"""
The idea in the solution is to go through the grid and whenever
you come across a floor tile, the number of rooms increases by one.
The room is then closed with # marks so that the room is not recalculated.

The fill function used in masonry is based on depth search: it first
masks the box given by the parameter and then continues masonry forward
to the adjacent squares in the width and vertical directions.
"""

def fill(house, y, x):
    if house[y][x] == "#":
        return
    house[y][x] = "#"
    fill(house, y-1, x)
    fill(house, y+1, x)
    fill(house, y, x-1)
    fill(house, y, x+1)

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