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

# Keeping track of the visited nodes and queue.
visited = []
queue = []

def bfs(visited, graph, node):
    """
    Parameter ´node´ sets the starting node. Function adds the
    ´node´ parameter to visited-list and to the queue. Funtion
    then loops all the neighbour nodes as long as there's nodes
    in the queue, and if not visited, adds it to visited-set
    and queue.
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
bfs(visited, graph, "1")