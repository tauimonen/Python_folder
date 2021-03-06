# Topological sort algorithm for directed acyclic graph (DAG)
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        # dict for adjacency list
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def topoSortUtil(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.topoSortUtil(i, visited, stack)

        stack.insert(0, v)

    def topoSort(self):
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if visited[i] == False:
                self.topoSortUtil(i, visited, stack)
        print(stack)


if __name__ == "__main__":
    g = Graph(11)
    g.addEdge(1, 3)
    g.addEdge(1, 5)
    g.addEdge(2, 1)
    g.addEdge(2, 5)
    g.addEdge(2, 6)
    g.addEdge(3, 5)
    g.addEdge(3, 7)
    g.addEdge(3, 10)
    g.addEdge(4, 3)
    g.addEdge(4, 6)
    g.addEdge(4, 7)
    g.addEdge(5, 8)
    g.addEdge(5, 9)
    g.addEdge(6, 5)
    g.addEdge(6, 9)
    g.addEdge(7, 6)
    g.addEdge(7, 8)
    g.addEdge(7, 10)
    g.addEdge(8, 9)
    g.topoSort()