class Network:
    def __init__(self, n):
        self.net = {}
        for i in range(1, n + 1):
            self.net[i] = []

    def add_link(self, a, b):
        self.net[a].append(b)
        self.net[b].append(a)

    def best_route(self, a, b):
        length = 0
        visited = []
        queue = []
        queue.append([a])
        if a == b:
            return length

        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node not in visited:
                visited.append(node)
                neighbours = self.net[node]
                for neighbour in neighbours:
                    shortest_path = list(path)
                    shortest_path.append(neighbour)
                    queue.append(shortest_path)
                    if neighbour == b:
                        return len(shortest_path) - 1
        return -1

if __name__ == "__main__":
    w = Network(5)
    w.add_link(1,2)
    w.add_link(2,3)
    w.add_link(1,3)
    w.add_link(4,5)
    print(w.best_route(1,5)) # -1
    w.add_link(3,5)
    print(w.best_route(1,5)) # 2