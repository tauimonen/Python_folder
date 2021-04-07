# Using a Python dict as an adjacency list for directed graph.
graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

# Keeping track of the visited nodes and queue.
visited = []
queue = []

def bfs(visited, graph, node):
    """
    Parameter ´node´ sets the starting node. Funtion loops all the
    neighbour nodes and if not in visited-set, prints it and adds to
    visited-set.
    :param visited: list
    :param graph: dict
    :param node: str
    :return: none
    """
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Driver code
bfs(visited, graph, "A")