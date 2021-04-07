# Using a Python dict as an adjacency list for directed graph.
graph = {
    "A": ["B", "C"],
    "B": ["D", "E:"],
    "C": ["F"],
    "D": [],
    "E": ["F"],
    "F": []
}

# Keeping track of the visited nodes.
visited = set()

def dfs(visited, graph, node):
    """
    Parameter ´node´ sets the starting node. Funtion loops all the
    neighbour nodes and if not in visited-set, prints it and adds to
    visited-set.
    :param visited: set
    :param graph: dict
    :param node: str
    :return: none
    """
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver code
dfs(visited, graph, "A")




