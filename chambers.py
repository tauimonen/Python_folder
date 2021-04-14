def dfs(grid, y, x):
    """
    Depth first search algorithm. Returns true when room parts
    changed from 0 to 1.
    :param grid: List of lists (binary)
    :param y: Start point y-coordinate, Int
    :param x: Start point x-coordinate, Int
    :return: Boolean
    """
    if grid[y][x] == 1:
        return

    grid[y][x] = 1  # Changes all visited boxes to 1
    dfs(grid, y-1, x)
    dfs(grid, y+1, x)
    dfs(grid, y, x-1)
    dfs(grid, y, x+1)
    return True

def count(r):
    """
    Counts and returns the amount of rooms (components) using
    convert- and dfs-funtions.
    :param r: List of lists (char)
    :return: Int
    """
    rooms = 0
    grid = convert(r)
    for i in range(len(r)):
        for j in range(len(r[0])):
            if grid[i][j] == 0:
                if dfs(grid, i, j):
                    rooms += 1
    return rooms

def convert(g):
    """
    Converts char grid to binary grid.
    :param g: List of lists containing chars "#" and ".".
    :return: List of lists containing ints 1 and 0.
    """
    n = len(g)
    grid = [[] for _ in range(n)]
    for i in range(n):
        for j in range(0, len(g[0])):
            if g[i][j] == "#":
                grid[i].append(1)
            else:
                grid[i].append(0)
    return grid


if __name__ == "__main__":
    r = ["########",
         "#..#...#",
         "####.#.#",
         "#..#.#.#",
         "########"]
    print(count(r)) # 3
