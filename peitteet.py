def empty_rect(grid, y, x, height, width):
    for i in range(height):
        for j in range(width):
            if grid[y+i][x+j]:
                return False
    return True

def fill_rect(grid, y, x, height, width, value):
    for i in range(height):
        for j in range(width):
            grid[y+i][x+j] = value

def search(grid, blocks, y, x):
    n, m = len(grid), len(grid[0])
    if y == n:
        return 1
    elif x == m:
        return search(grid, blocks, y+1, 0)
    elif grid[y][x]:
        return search(grid, blocks, y, x+1)
    elif blocks == 0:
        return 0
    else:
        sum = 0
        for i in range(1, n-y+1):
            for j in range(1, m-x+1):
                if empty_rect(grid, y, x, i, j):
                    fill_rect(grid, y, x, i, j, 1)
                    sum += search(grid, blocks-1, y, x+1)
                    fill_rect(grid, y, x, i, j, 0)
        return sum

def count(n, m, k):
    grid = [[0]*m for _ in range(n)]
    return search(grid, k, 0, 0)


if __name__ == "__main__":
    print(count(2,2,4)) # 8
    print(count(2,3,3)) # 13
    print(count(4,4,1)) # 1
    print(count(4,3,10)) # 3146
    print(count(4,4,16)) # 70878