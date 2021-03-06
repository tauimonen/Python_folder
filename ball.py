class Ball:
    """
    Class for calculating the maximum amount of pairs that can be formed.
    Using Ford-Fulkerson and breadth-first search.
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



if __name__ == "__main__":
    b = Ball(4)
    print(b.calculate())  # 0
    b.add_pair(1, 2)
    print(b.calculate())  # 1
    b.add_pair(1, 3)
    b.add_pair(3, 2)
    print(b.calculate())  # 2

    print(20 * "=")

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
