from collections import defaultdict
import heapq


def create_spanning_tree(graph, starting_vertex):
    mst = defaultdict(set)
    visited = set([starting_vertex])
    edges = [
        (cost, starting_vertex, to)
        for to, cost in graph[starting_vertex].items()
    ]
    heapq.heapify(edges)

    while edges:
        cost, frm, to = heapq.heappop(edges)
        if to not in visited:
            visited.add(to)
            print(to)
            mst[frm].add(to)
            for to_next, cost in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (cost, to, to_next))

    return mst

example_graph = {
    'A': {'B': 15, 'C': 8, 'E': 14},
    'B': {'A': 15, 'E': 2, 'D': 9, 'G': 5},
    'C': {'A': 8, 'G': 12},
    'D': {'B': 9, 'F': 11, 'G': 13},
    'E': {'A': 14, 'B': 2, 'F': 7},
    'F': {'D': 11, 'E': 5, 'G': 4},
    'G': {'B': 5, 'C': 12, 'D': 13, 'F': 4},
}

a = dict(create_spanning_tree(example_graph, 'A'))
print(a)
