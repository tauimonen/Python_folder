
def count(r):
    """
    The function calculates how many squares at least need to be turned into a wall
    so that there is no path in the grid from the top left to the bottom right.
    Using class C and its functions.
    :param r: list of strings
    :return: int
    """
    n = len(r)
    f = C(n ** 2)
    for y in range(n):
        for x in range(n):
            if r[y][x] != '.':
                continue
            if x < n-1 and r[y][x + 1] == '.':
                f.add_teleport((y * n) + x, (y * n) + x + 1, 1)
            if y < n-1 and r[y+1][x] == '.':
                f.add_teleport((y * n) + x, ((y + 1) * n) + x, 1)
    res = f.calculate(0, n ** 2 - 1)
    return res

class C:
    """
    Class for calculating the maximum amount of teleports needed to
    go from a planet 1 to planet n. Using Ford-Fulkerson and breadth-first search.
    """
    def __init__(self,n):
        self.n = n + 1
        self.graph = [[] for _ in range(self.n)]
        self.limits = [[0] * self.n for _ in range(self.n)]

    def add_teleport(self, a, b, x=1):
        self.graph[a].append(b)
        self.limits[a][b] += x

    def calculate(self, a, b):
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
                if self.limits[jonosta][n] - v[jonosta][n] > 0 and p[n] == -1:
                    p[n] = jonosta
                    t[n] = min(t[jonosta], self.limits[jonosta][n] - v[jonosta][n])
                    if n == b:
                        return t[b], p
                    else:
                        jono.append(n)
        return 0, p



if __name__ == "__main__":
    r = [".....",
         ".###.",
         "...#.",
         "##.#.",
         "....."]
    print(count(r)) # 2
    r2 = [".....",
         ".....",
         "..#.#",
         ".....",
         "..#.."]
    print(count(r2))  # 2