"""
Cheks if all the possible spanning trees have the same weight.
"""


class SameWeight:
    def __init__(self, n):
        self.n = n
        self.edges = []

    def add_edge(self, a, b, x):
        self.edges.append((x, a, b))

    def find(self, x):
        while self.link[x] != x:
            x = self.link[x]
        return x

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.size[a] += self.size[b]
        self.link[b] = a

    def mst(self, rev):
        self.link = list(range(self.n + 1))
        self.size = [1] * (self.n + 1)
        self.edges.sort()
        if rev:
            self.edges.reverse()
        cost = 0
        count = self.n
        for edge in self.edges:
            if self.find(edge[1]) != self.find(edge[2]):
                self.union(edge[1], edge[2])
                cost += edge[0]
                count -= 1
        return cost if count == 1 else -1

    def check(self):
        return self.mst(False) == self.mst(True)


if __name__ == "__main__":
    s = SameWeight(4)
    s.add_edge(1,2,2)
    s.add_edge(1,3,3)
    print(s.check()) # True
    s.add_edge(1,4,3)
    print(s.check()) # True
    s.add_edge(3,4,3)
    print(s.check()) # True
    s.add_edge(2,4,1)
    print(s.check()) # False