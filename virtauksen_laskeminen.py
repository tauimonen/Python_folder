
def add_edge(a, b, x):
    graph[a][b] += x


n = 5
graph = [[0] * (n + 1) for _ in range(n + 1)]
add_edge(1, 3, 4)
add_edge(1, 2, 3)
add_edge(2, 4, 8)
add_edge(3, 4, 2)
add_edge(4, 5, 3)

print(graph)