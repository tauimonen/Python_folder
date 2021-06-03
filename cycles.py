"""The solution checks whether there is a directed cycle in the
network."""

from collections import defaultdict

class Cycles:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.n = vertices + 1

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def check(self):
        visited = [0] * self.n
        s = []
        for i in range(self.n):
            for j in self.graph[i]:
                visited[j] += 1
        for i in range(len(visited)):
            if visited[i] == 0:
                s.append(i)
        count = 0
        while s:
            y = s.pop(0)
            for v in self.graph[y]:
                visited[v] -= 1
                if visited[v] == 0:
                    s.append(v)
            count += 1
        for i in self.graph:
            if i in self.graph[i]:
                return True
        if count == self.n:
            return False
        else:
            return True


if __name__ == "__main__":
    c = Cycles(5)
    c.add_edge(1, 2)
    c.add_edge(2, 3)
    c.add_edge(1, 3)
    c.add_edge(3, 4)
    print(c.check())  # False
    c.add_edge(4, 2)
    print(c.check()) # True



