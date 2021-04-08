"""
Grid handling with show-function, dfs-algorithm and kind of
animation.
"""

from time import sleep


grid = [[1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1]]


def show(y, x):
    print("\n"*50)  # Part of "animation"
    n = len(grid)
    m = len(grid[0])
    for i in range(0, n):
        s = " "
        for j in range(0, m):
            if i == y and j == x:
                s += "@"            # Moving part
            elif grid[i][j] == 0:
                s += "."
            else:
                s += "#"
        print(s)
    print()
    sleep(0.5)  # Part of "animation"


my_y = 4
my_x = 6
show(my_y, my_x)

def dfs(y, x):
    if grid[y][x] == 1:
        return
    show(y, x)
    grid[y][x] = 1  # Changes all visited boxes to 1
    dfs(y-1, x)
    dfs(y+1, x)
    dfs(y, x-1)
    dfs(y, x+1)


dfs(my_y, my_x)

