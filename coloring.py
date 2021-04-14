class Coloring:
    def __init__(self, n):
        self.n = n
        self.visited = [0 for _ in range(self.n + 1)]
        self.graph = [[] for _ in range(self.n + 1)]
        self.color = [0 for _ in range(self.n + 1)]
        self.visited[1] = True
        self.color[1] = 0

    def add_edge(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)

    def dfs(self, graph, visited, m, color):
        for i in graph[m]:
            if not visited[i]:
                visited[i] = True
                color[i] = not color[m]
                if not self.dfs(graph, visited, i, color):
                    return False
            elif color[i] == color[m]:
                return False
        return True

    def check(self):
        self.visited = [0 for _ in range(self.n + 1)]
        for i in range(self.n):
            if not self.dfs(self.graph, self.visited, i, self.color):
                return False
        return True



if __name__ == "__main__":
    c = Coloring(5)
    c.add_edge(4, 5)
    c.add_edge(2, 3)
    c.add_edge(3, 5)
    c.add_edge(1, 3)
    print(c.check()) # True

    c = Coloring(5)
    c.add_edge(4, 5)
    c.add_edge(2, 3)
    print(c.check())
    c.add_edge(3, 5)

    c.add_edge(1, 3)

    print(c.check())

    c = Coloring(4)
    c.add_edge(1, 2)
    c.add_edge(2, 3)
    c.add_edge(3, 4)
    c.add_edge(1, 4)
    c.add_edge(2, 4)
    print(c.check())  # False
    #
    c = Coloring(5)
    c.add_edge(4, 5)
    c.add_edge(2, 3)
    c.add_edge(3, 5)
    c.add_edge(1, 3)
    print(c.check()) # True

    #
    c = Coloring(5)
    c.add_edge(3, 4)
    c.add_edge(4, 5)
    c.add_edge(4, 5)
    c.add_edge(4, 5)
    c.add_edge(3, 5)
    print(c.check())  # False



