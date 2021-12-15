class Ball:
    """
    Class for calculating the maximum amount of pairs that can be formed.
    Using Ford-Fulkerson and breadth-first search.

    NOT WORKING! Should maybe somehow detect cycles first.
    """
    def __init__(self,n):
        self.n = n + 1
        self.graph = [[] for _ in range(self.n)]
        self.limits = [[0] * self.n for _ in range(self.n)]
        self.starts = []
        self.ends = []

    def add_pair(self, a, b, x=1):
        if a == b:
            return

        self.graph[a].append(b)
        self.limits[a][b] += x
        self.starts.append(a)
        self.ends.append(b)

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
        if not self.starts or not self.ends:
            return 0
        for i in self.starts:
            for j in self.ends:
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

    print(20*"=")

    b = Ball(5)
    print(b.calculate())
    b.add_pair(5, 5)
    print(b.calculate())
    b.add_pair(3, 4)
    print(b.calculate())
    print(b.calculate())
    print(b.calculate())
    b.add_pair(1, 3)
    b.add_pair(4, 2)
    print(b.calculate())
    b.add_pair(5, 3)
    b.add_pair(5, 1)
    b.add_pair(1, 4)
    b.add_pair(1, 2)
    b.add_pair(1, 3)
    print(b.calculate())
    print(b.calculate())

    b.add_pair(4, 5)
    print(b.calculate())
    b.add_pair(2, 5)
    b.add_pair(5, 5)
    print(b.calculate())
    print(b.calculate())
    print(b.calculate())
    b.add_pair(3, 1)
    print(b.calculate())
    print(b.calculate())
    b.add_pair(5, 3)
    print(b.calculate())
    b.add_pair(3, 5)
