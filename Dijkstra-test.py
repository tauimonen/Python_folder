import random
import timeit
import heapq


class Graph:
    def __init__(self, n):
        self.graph = [[] for _ in range(n)]
        self.n = n
        for a in range(2, n):
            for b in range(2, n):
                if a < b and b - a < 10:
                    weight = random.randint(1, 1000)
                    self.graph[a].append((b, weight))

    def dijkstra(self):
        distances = [float('inf') for vertex in self.graph]
        distances[1] = 0
        pq = [(0, 1)]
        while len(pq) > 0:
            current_distance, current_vertex = heapq.heappop(pq)
            if current_distance > distances[current_vertex]:
                continue
            for neighbor, weight in self.graph[current_vertex]:
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
