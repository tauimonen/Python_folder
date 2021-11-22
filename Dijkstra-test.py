import random
import timeit
import heapq

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

    def dijkstra(self):
        distances = {vertex: float('inf') for vertex in self.graph}
        distances[1] = 0
        pq = [(0, 1)]

        while len(pq) > 0:
            current_distance, current_vertex = heapq.heappop(pq)
            if current_distance > distances[current_vertex]:
                continue
            for neighbor, weight in self.graph[current_vertex].items():
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
        return min(distances)


if __name__ == "__main__":
    graph = Graph(5000)
    start_time = timeit.default_timer()
    print("The start time is :", start_time)
    graph.dijkstra()
    print("The time difference is :", timeit.default_timer() - start_time)
