class Shortening:
    def __init__(self, n):
        self.n = n
        self.graph = []

    def add_edge(self, a, b, x):
        self.graph.append((a - 1, b - 1, x))

    def check(self, a, b):
        distance = [float('inf')] * self.n
        distance[1] = 0
        count = 0
        edges = []
        for edge in self.graph:
            if (edge[0] == a and edge[1] == b) or edge[1] == b:
                edges.append(edge)

        while True:
            found = False
            for edge in edges:
                if distance[edge[1]] > distance[edge[0]] + edge[2]:
                    distance[edge[1]] = distance[edge[0]] + edge[2]
                    found = True
                    if edge[1] == b - 1 and count >= self.n:
                        return True
            count += 1
            if not found or self.n <= 3:
                return False
            else:
                return True


if __name__ == "__main__":
    s = Shortening(5)
    print(s.check(3, 4))
    print(s.check(5, 3))
    s.add_edge(3, 4, 3)
    print(s.check(3, 5))
    s.add_edge(4, 1, 9)
    print(s.check(2, 3))
    print(s.check(4, 3))
    print(s.check(2, 1))
    s.add_edge(3, 1, -4)
    s.add_edge(2, 4, 8)
    print(s.check(5, 3))
    print(s.check(4, 1))
    print(s.check(2, 5))
    print(s.check(4, 5))
    print(s.check(5, 3))
    s.add_edge(2, 3, -5)
    s.add_edge(2, 4, 7)
    s.add_edge(4, 2, 1)
    s.add_edge(3, 4, -9)
    print(s.check(4, 5))