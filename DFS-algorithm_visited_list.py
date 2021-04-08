n = 5
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

def add_edge(a, b):
    graph[a].append(b)
    graph[b].append(a)

def dfs(x):
    if visited[x]:
        return
    visited[x] = True
    print("tultiin solmuun", x)
    for y in graph[x]:
        dfs(y)

add_edge(1, 2)
add_edge(1, 3)
add_edge(2, 4)
add_edge(3, 4)
add_edge(4, 5)
print(graph)
dfs(3)



