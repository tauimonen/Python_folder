import heapq

def calculate_distances(graph, starting_vertex):
    distances = {vertex: float('inf') for vertex in graph}
    distances[starting_vertex] = 0
    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)
        if current_distance > distances[current_vertex]:
            continue
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    return min(distances)


example_graph = {
    '1': {'2': 10, '4': 2},
    '2': {'3': 10, '5': 2},
    '3': {'6': 2},
    '4': {'2': 3, '5': 8},
    '5': {'3': 3, '6': 8},
    '6': {}
}
start = '1'
print(calculate_distances(example_graph, start))
