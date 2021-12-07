class LongPath:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n + 1)]

    def add_edge(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)

    def dfs(self, x):
        
        if x in self.mem:
            return self.mem[x]
        l = 0
        for y in self.graph[x]:
            if y > x:
                l = max(l, self.dfs(y) + 1)
        self.mem[x] = l

        return l

    def calculate(self):
        res = 0
        self.mem = {}
        for i in range(1, self.n + 1):
            res = max(res, self.dfs(i))

        return res


if __name__ == "__main__":
    l = LongPath(4)
    l.add_edge(1, 2)
    l.add_edge(1, 3)
    l.add_edge(2, 4)
    l.add_edge(3, 4)
    print(l.calculate())    # 2
    l.add_edge(3, 2)
    print(l.calculate())    # 3
