class Graph:
    def __init__(self, node_count):
        self.node_count = node_count
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def tulosta(self, distance):
        print("Distance")
        for i in range(self.node_count):
            print("{0}\t\t{1}".format(i, distance[i]))

    def bf(self, start):
        distance = [float("Inf")] * self.node_count
        distance[start] = 0

        for _ in range(self.node_count - 1):
            for u, v, w, in self.graph:
                if distance[u] != float("Inf") and distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
                    print(v, "distance: ", distance[v])

        for u, v, w in self.graph:
            if distance[u] != float("Inf") and distance[u] + w < distance[v]:
                print("Negative cycle")
                return

        self.tulosta(distance)


graph = Graph(6)
graph.add_edge(0, 1, 10)
graph.add_edge(0, 3, 2)
graph.add_edge(1, 2, 10)
graph.add_edge(1, 4, 2)
graph.add_edge(2, 5, 2)
graph.add_edge(3, 1, 3)
graph.add_edge(3, 4, 8)
graph.add_edge(4, 2, 3)
graph.add_edge(4, 5, 8)

graph.bf(0)
