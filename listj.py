from heapq import heappush, heappop


def dijkstra(graph, start, end):
    n = len(graph)
    ready = [False] * n
    distances = [float('inf')] * n
    distances[start] = 0
    heap = []
    heappush(heap, (0, start))
    while len(heap) > 0:
        vertex = heappop(heap)[1]
        if ready[vertex]:
            continue
        ready[vertex] = True
        for edge in graph[vertex]:
            if distances[vertex] + edge[1] < distances[edge[0]]:
                distances[edge[0]] = distances[vertex] + edge[1]
                heappush(heap, (distances[vertex] + edge[1], edge[0]))

    return distances[end]


def calculate(t):
    n = len(t)
    if t[0] >= n:
        return -1
    graph = [[] for _ in range(n)]
    for i in range(len(t)):
        if i - t[i] >= 0:
            graph[i].append((i - t[i], t[i]))
        if i + t[i] < len(t):
            graph[i].append((i + t[i], t[i]))
    res = dijkstra(graph, 0, n - 1)

    return res


if __name__ == "__main__":
    print(calculate([1,1,1,1])) # 3
    print(calculate([3,2,1])) # -1
    print(calculate([3,5,2,2,2,3,5])) # 10
    print(calculate([7,5,3,1,4,2,4,6,1])) # 32