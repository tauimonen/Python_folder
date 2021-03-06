from collections import defaultdict


class Download:

    def __init__(self, n):
        self.n = n + 1
        self.graph = [[0] * (n + 1) for _ in range(n + 1)]
        self.max_flow = 0

    def add_link(self, a, b, x):
        self.graph[a][b] += x

    def bfs(self, s, t, parent):
        visited = [False] * self.n
        queue = []
        queue.append(s)
        visited[s] = True

        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        return True if visited[t] else False

    def calculate(self, source, sink):
        parent = [-1] * self.n

        while self.bfs(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
            self.max_flow += path_flow
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return self.max_flow


if __name__ == "__main__":
    d = Download(4)
    print(d.calculate(1,4)) # 0
    d.add_link(1,2,5)
    d.add_link(2,4,6)
    d.add_link(1,4,2)
    print(d.calculate(1,4)) # 7
    d.add_link(1,3,4)
    d.add_link(3,2,2)
    print(d.calculate(1,4)) # 8
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
