def count_cycles(graph, start, visited):
    visited[start] = True
    count = 0
    for next in graph[start]:
        if not visited[next]:
            count += count_cycles(graph, next, visited)
        elif start != next:
            count += 1
    return count

if __name__ == "__main__":
    graph = {
        3: {10},
        4: {8},
        6: {3},
        7: {4, 6},
        8: {7},
        10: {6}
    }
    visited = [False] * (max(graph)+1)
    print(count_cycles(graph, 8, visited))
