"""Solution for unique paths problem. Grid dimensions are m x n and path starts from
top-left corner and ends to the bottom-right corner."""

class Solution:
    def uniquePaths(self, m: int, n: int):
        rows = n
        columns = m

        # Creating 0-grid n x m
        grid = [[0] * m for _ in range(columns)]

        # Filling with ones
        for i in range(rows):
            grid[i][0] = 1

        for j in range(columns):
            grid[0][j] = 1

        # Counting all the values in the grid by summing above and left values
        # when loopping the whole grid
        for row in range(1, rows):
            for col in range(1, columns):
                above_value = grid[row-1][col]
                left_value = grid[row][col-1]
                grid[row][col] = above_value + left_value

        return grid[rows-1][columns-1]


s = Solution
print(s.uniquePaths(s, 4, 3))