# Using a Python dict as an adjacency list for directed graph.
graph = {
    "1": ["6"],
    "2": ["1", "6"],
    "3": ["2"],
    "4": ["3", "7"],
    "5": ["4"],
    "6": ["3", "4"],
    "7": ["5"]
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
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver code
dfs(visited, graph, "1")




