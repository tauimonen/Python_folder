class C:
    """
    Class for calculating the maximum amount of teleports needed to
    go from a planet 1 to planet n. Using Ford-Fulkerson and breadth-first search.
    """
    def __init__(self,n):
        self.n = n + 1
        self.graph = [[] for _ in range(self.n)]
        self.limits = [[0] * self.n for _ in range(self.n)]

    def add_pair(self, a, b, x=1):
        self.graph[a].append(b)
        self.limits[a][b] += x

    def calculate(self, a, b):
        print(self.graph)
        maxim = 0
        memo = [[0] * self.n for _ in range(self.n)]
        while True:
            m, p = self.bfs(a, b, memo)
            if m == 0:
                return maxim
            maxim += m
            v = b

            while v != a:

                u = p[v]
                memo[u][v] += m
                memo[v][u] -= m
                v = u



    def bfs(self, a, b, v):
        jono = []
        p = [-1] * self.n
        t = [10**9] * self.n
        jono.append(a)
        while jono:
            jonosta = jono.pop()
            for n in self.graph[jonosta]:
                if self.limits[jonosta][n] - v[jonosta][n] > 0 and p[n] == - 1:
                    p[n] = jonosta
                    t[n] = min(t[jonosta], self.limits[jonosta][n] - v[jonosta][n])
                    if n == b:
                        return t[b], p
                    else:
                        jono.append(n)
        return 0, p

def count(r):

    n = len(r)
    f = C(n)
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