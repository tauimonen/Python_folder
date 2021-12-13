
def add_edge(a, b, x):
    graph[a][b] += x

def dfs(start, goal):
    global found, result
    if visited[start]:
        return
    path.append(start)
    visited[start] = True
    if start == goal and not found:
        found = True
        result = path[:]
    for i in range(1, n + 1):
        if graph[start][i] > 0:
            dfs(i, goal)
    path.pop()

n = 7
graph = [[0] * (n + 1) for _ in range(n + 1)]
add_edge(1, 5, 15)
add_edge(1, 2, 7)
add_edge(2, 3, 3)
add_edge(2, 4, 2)
add_edge(3, 7, 8)
add_edge(4, 3, 4)
add_edge(4, 7, 3)
add_edge(5, 4, 3)
add_edge(5, 6, 9)
add_edge(5, 4, 5)
add_edge(6, 7, 5)

visited = [False] * (n + 1)
path = []
found = False
result = []
dfs(1, 5)
print(found)
print(result)
min_weight = 10**9
for i in range(len(result) - 1):
    print(result[i], result[i+1], graph[result[i]][result[i+1]])
    min_weight = min(min_weight, graph[result[i]][result[i+1]])
print(min_weight)
for i in range(len(result) - 1):
    graph[result[i]][result[i+1]] -= min_weight
    graph[result[i+1]][result[i]] += min_weight  # the return direction increases

print(graph)
