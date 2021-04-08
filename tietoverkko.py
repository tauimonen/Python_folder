class Network:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(self.n + 1)]

    def add_link(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)

    def best_route(self, a, b):
        self.dist = [-1] * (self.n + 1)
        self.dist[a] = 0
        queue = [a]
        i = 0
        while i < len(queue):
            x = queue[i]
            for y in self.graph[x]:
                if self.dist[y] == -1:
                    self.dist[y] = self.dist[x] + 1
                    queue.append(y)
            i += 1
        return self.dist[b]


if __name__ == "__main__":
    w = Network(5)
    w.add_link(1,2)
    w.add_link(2,3)
    w.add_link(1,3)
    w.add_link(4,5)
    print(w.best_route(1,5)) # -1
    w.add_link(3,5)
    print(w.best_route(1,5)) # 2