# Topological sort algorithm for directed acyclic graph (DAG)
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