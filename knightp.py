class Ball:
    """
    Class for calculating the maximum amount of pairs that can be formed.
    Using Ford-Fulkerson and breadth-first search.

    NOT WORKING YET!
    """

    def __init__(self, n):
        self.n = n
        self.nn = (2 * n) + 2
        self.graph = [[0] * self.nn for _ in range(self.nn)]
        self.f = [x[:] for x in self.graph]
        self.visited = [False] * self.nn

    def add_pair(self, a, b):
        self.graph[a][b + self.n] = 1
        self.graph[b + self.n][-1] = 1
        self.graph[0][a] = 1

    def calculate(self):
        res = 0
        self.f = [x[:] for x in self.graph]
        while True:
            self.visited = [False] * self.nn
            flow = self.bfs(0, self.nn - 1, 10 ** 9)
            if flow == 0:
                return res
            res += flow

    def bfs(self, a, b, v):
        if self.visited[a]:
            return 0
        self.visited[a] = True
        if a == b:
            return v
        for i in range(len(self.graph)):
            if self.f[a][i] > 0:
                flow = self.bfs(i, b, min(v, self.f[a][i]))
                if flow > 0:
                    self.f[a][i] -= flow
                    self.f[i][a] += flow
                    return flow
        return 0

def count(r):

    n = len(r)
    f = Ball(n)
    cou = 0
    grid = [[0] * (n) for _ in range(n)]
    val = 1
    for i in range(0, n ):
        for j in range(0, n):
            grid[i][j] = val
            val += 1
    print(grid)
    for y in range(1, n):
        for x in range(1, n):
            if r[y][x] != '.':
                continue
            if r[y][x] == '*':
                for move in [(y+1, x+2), (y+2, x+1), (y+1, x-2), (y+2, x-1),
                             (y-1, x+2), (y-2, x+1), (y-1, x-2), (y-2, x-1)]:
                    if r[move[0]][move[1]] == "*":
                        cou += 1
                        f.add_pair(grid[move[0]][move[1]])

    return f.calculate(1, n * n)



if __name__ == "__main__":
    r = ["*.......",
         "..*...*.",
         "........",
         ".*......",
         "...*....",
         ".......*",
         "........",
         "......*."]
    print(count(r)) # 3