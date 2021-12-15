class C:
    """
    Class for calculating the maximum amount of teleports needed to
    go from a planet 1 to planet n. Using Ford-Fulkerson and breadth-first search.

    Not working yet!
    """



    def __init__(self,n):
        self.n = n + 1
        self.graph = [[] for _ in range(self.n)]
        self.limits = [[0] * self.n for _ in range(self.n)]

    def add_pair(self, a, b, x=1):
        self.graph[a].append(b)
        self.limits[a][b] += x

    def calculate(self, a=1):
        b = self.n - 1
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

    def count(self, r):
        n = len(r) + 1
        for y in range(n):
            for x in range(n):
                if r[x][y] == "*":
                    for move in [(x + 1, y + 2), (x + 2, y + 1), (x - 2, y + 1), (x - 1, y + 2)]:
                        if r[move[0]][move[1]] == "*":
                            self.add_pair((x, y), move)
        return self.graph





if __name__ == "__main__":

    r = ["*.......",
         "..*...*.",
         "........",
         ".*......",
         "...*....",
         ".......*",
         "........",
         "......*."]
    c = C(len(r))
    print(c.count(r)) # 3