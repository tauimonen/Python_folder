from collections import deque
from math import inf

class Download:
    def __init__(self,n):
        self._n = n+1
        self._graph = [[] for _ in range(self._n)]
        self._cap = [[0]*self._n for _ in range(self._n)]

    def add_link(self,a,b,x):
        self._graph[a].append(b)
        self._cap[a][b] += x

    def _bfs(self, a, b, flows):
        queue = deque()
        parent = [-1]*self._n
        m = [inf]*self._n
        queue.append(a)
        while not len(queue) == 0:
            node = queue.popleft()
            for neighbour in self._graph[node]:
                if self._cap[node][neighbour] - flows[node][neighbour] > 0 and parent[neighbour] == -1:
                    parent[neighbour] = node
                    m[neighbour] = min(m[node], self._cap[node][neighbour] - flows[node][neighbour])
                    if neighbour == b:
                        return m[b], parent
                    queue.append(neighbour)
        return 0, parent

    def calculate(self,a,b):
        f = 0
        flows = [[0]*self._n for _ in range(self._n)]
        while True:
            m, p = self._bfs(a, b, flows)
            if m == 0:
                return f
            f += m
            v = b
            while v != a:
                u = p[v]
                flows[u][v] += m
                flows[v][u] -= m
                v = u

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