
class Download:
    """
    Class for calculating the maximum amount of data that can be transmitted
    from a given computer to another in a second in a given network.
    Using Ford-Fulkerson and breadth-first search.
    """
    def __init__(self,n):
        self.n = n + 1
        self.graph = [[] for _ in range(self.n)]
        self.limits = [[0] * self.n for _ in range(self.n)]

    def add_link(self, a, b, x):
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

    print("========")
    d = Download(5)
    print(d.calculate(3, 4))
    d.add_link(5, 3, 6)
    print(d.calculate(5, 4))
    print(d.calculate(4, 5))
    print(d.calculate(5, 1))
    d.add_link(5, 4, 9)
    d.add_link(1, 2, 10)
    print(d.calculate(3, 1))
    print(d.calculate(2, 4))
    print(d.calculate(5, 4))
    d.add_link(5, 2, 9)
    print("seuraava 0")
    print(d.calculate(1, 5)) # 0
    d.add_link(3, 5, 2)
    d.add_link(1, 3, 2)
    d.add_link(5, 4, 9)
    print(d.calculate(5, 4))
    print(d.calculate(2, 3))
    print(d.calculate(1, 3))
    print(d.calculate(3, 2))
    print(d.calculate(5, 4))
    print(d.calculate(4, 5))
    d.add_link(4, 3, 9)
    print(d.calculate(4, 5))
    print(d.calculate(2, 4))
    print(d.calculate(4, 5))
    d.add_link(5, 1, 6)
    d.add_link(3, 5, 3)
    d.add_link(4, 5, 2)
    print(d.calculate(3, 4))
    d.add_link(5, 3, 3)
    print("======")

    d = Download(5)
    print(d.calculate(3, 4))
    d.add_link(5, 3, 6)
    print(d.calculate(5, 4))
    print(d.calculate(4, 5))
    print(d.calculate(5, 1))
    d.add_link(5, 4, 9)
    d.add_link(1, 2, 10)
    print(d.calculate(3, 1))
    print(d.calculate(2, 4))
    print(d.calculate(5, 4))
    d.add_link(5, 2, 9)
    print(d.calculate(1, 5))
    d.add_link(3, 5, 2)
    d.add_link(1, 3, 2)
    d.add_link(5, 4, 9)
    print("seuraava 18")
    print(d.calculate(5, 4)) # 18
    print(d.calculate(2, 3))
    print(d.calculate(1, 3))
    print(d.calculate(3, 2))
    print(d.calculate(5, 4))
    print(d.calculate(4, 5))
    d.add_link(4, 3, 9)
    print(d.calculate(4, 5))
    print(d.calculate(2, 4))
    print(d.calculate(4, 5))
    d.add_link(5, 1, 6)
    d.add_link(3, 5, 3)
    d.add_link(4, 5, 2)
    print(d.calculate(3, 4))
    d.add_link(5, 3, 3)
