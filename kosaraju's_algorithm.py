"""The Kosaraju's algorithm is a powerful algorithm that forms a
directed network strongly congruent components. The algorithm has
two steps, each go through the network nodes with depth search.
The first step is reminiscent finding the topological order and
generating a list of nodes. The second step forms strongly uniform
components based on this list."""

from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        # dict for adjacency list
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtil(self, v, visited):
        visited[v] = True
        print(v)
        for i in self.graph[v]:
            if visited[i] == False:
                self.DFSUtil(i, visited)

    def topoSortUtil(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if visited[i] == False:
                self.topoSortUtil(i, visited, stack)
        stack.append(v)

    def getTranspose(self):
        g = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)
        return g

    def printSCCs(self):
        """Prints strongly connected components"""
        visited = [False] * self.V
        stack = []
        for i in range(self.V):
            if visited[i] == False:
                self.topoSortUtil(i, visited, stack)

        gr = self.getTranspose()
        visited = [False] * self.V

        while stack:
            i = stack.pop()
            if visited[i] == False:
                gr.DFSUtil(i, visited)
                print()


if __name__ == "__main__":
    g = Graph(8)
    g.addEdge(1, 6)
    g.addEdge(2, 1)
    g.addEdge(2, 5)
    g.addEdge(2, 7)
    g.addEdge(3, 1)
    g.addEdge(4, 5)
    g.addEdge(5, 4)
    g.addEdge(6, 3)
    g.addEdge(6, 4)
    g.addEdge(7, 2)
    g.addEdge(7, 4)
    g.printSCCs()