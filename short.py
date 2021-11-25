class Shortening:
    def __init__(self, n):
        self.n = n
        self.graph = []

    def add_edge(self, a, b, x):
        self.graph.append((a, b, x))

    def check(self, a, b):
        distance = [float('inf')] * self.n
        distance[a] = 0
        count = 0
        while True:
            found = False
            for edge in self.graph:
                if distance[edge[1]] > distance[edge[0]] + edge[2]:
                    distance[edge[1]] = distance[edge[0]] + edge[2]
                    found = True
                    if edge[1] == b and count >= self.n:
                        return True
            count += 1
            if not found or self.n <= 3:
                return False


if __name__ == "__main__":
    s = Shortening(5)
    print(s.check(1,3)) # False
    s.add_edge(1,2,5)
    s.add_edge(2,3,-2)
    print(s.check(1,3)) # False
    s.add_edge(2,4,1)
    s.add_edge(4,2,-2)
    print(s.check(1,3)) # True