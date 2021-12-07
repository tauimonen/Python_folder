class LongPath:
    def __init__(self,n):
        self.n = n
        self.und_graph = [[] for _ in range(0, n + 1)]


    def add_edge(self,a,b):
        self.und_graph[a].append(b)
        self.und_graph[b].append(a)

    def dfs(self, node):
        l = 0
        if node in self.lenghts:
            return self.lenghts[node]
        for i in self.und_graph[node]:
            if i > node:
                self.lenghts[node] = max(l, self.res[i] + 1)
            else:
                self.lenghts[node] = 0
        return self.lenghts[node]


    def calculate(self):
        self.lenghts = {}
        for i in range(1, self.n +1):
            r = max(0, self.res[i])
        return r



if __name__ == "__main__":
    l = LongPath(4)
    l.add_edge(1,2)
    l.add_edge(1,3)
    l.add_edge(2,4)
    l.add_edge(3,4)
    print(l.calculate()) # 2
    l.add_edge(3,2)
    print(l.calculate()) # 3