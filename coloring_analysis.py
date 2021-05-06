class Coloring:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(self.n + 1)]

    def add_edge(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)

    def dfs(self, x, c):
        if self.color[x] == c:
            return
        if self.color[x] == 3 - c:
            self.good = False
            return
        self.color[x] = c
        for y in self.graph[x]:
            self.dfs(y, 3 - c)

    def check(self):
        self.color = [0 for _ in range(self.n + 1)]
        self.good = True
        for i in range(1, self.n + 1):
            if not self.color[i]:
                self.dfs(i, 1)
        return self.good


if __name__ == "__main__":
    c = Coloring(4)
    c.add_edge(1,2)
    c.add_edge(2,3)
    c.add_edge(3,4)
    c.add_edge(1,4)
    print(c.check()) # True
    c.add_edge(2,4)
    print(c.check()) # False

