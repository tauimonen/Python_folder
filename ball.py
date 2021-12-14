class Ball:
    """
    Class for calculating the maximum amount of pairs that can be formed.
    Using Ford-Fulkerson and breadth-first search.
    """
    def __init__(self,n):
        self.n = n + 1
        self.graph = [[] for _ in range(self.n)]
        self.limits = [[0] * self.n for _ in range(self.n)]

    def add_pair(self, a, b, x=1):
        self.graph[a].append(b)
        self.limits[a][b] += x

    def calc(self, a, b):
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

    def calculate(self):
        m = 0
        for i in range(1, self.n):
            for j in range(1, self.n):
                m = max(m, self.calc(i, j))
        return m


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
    b = Ball(4)
    print(b.calculate()) # 0
    b.add_pair(1,2)
    print(b.calculate()) # 1
    b.add_pair(1,3)
    b.add_pair(3,2)
    print(b.calculate()) # 2