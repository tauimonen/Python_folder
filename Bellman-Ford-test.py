import random
import timeit


class Graph:
    def __init__(self, node_count):
        self.node_count = node_count
        self.graph = []
        self.distance = [float('inf')] * node_count
        self.distance[0] = 0
        self.edges = []
        for a in range(2, node_count):
            for b in range(2, node_count):
                if a < b and b - a < 10:
                    weight = random.randint(1, 1000)
                    self.edges.append((a, b, weight))

    def bf(self):
        count = 0
        while True:
            change = False
            for edge in self.edges:
                now = self.distance[edge[1]]
                new = self.distance[edge[0]] + edge[2]
                if new < now:
                    self.distance[edge[1]] = new
                    change = True
            if not change:
                break


if __name__ == "__main__":
    graph = Graph(5000)
    start_time = timeit.default_timer()
    print("The start time is :", start_time)
    graph.bf()
    print("The time difference is :", timeit.default_timer() - start_time)
