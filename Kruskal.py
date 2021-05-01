from collections import defaultdict

class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def KruskalMST(self):
        result = []
        i = 0
        e = 0
        self.graph = sorted(self.graph,
                            key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        minimumCost = 0
        print("Edges in the constructed MST")
        for u, v, weight in result:
            minimumCost += weight
            print("%d -- %d == %d" % (u, v, weight))
        print("Minimum Spanning Tree", minimumCost)


g = Graph(7)
g.addEdge(0, 1, 15)
g.addEdge(0, 2, 8)
g.addEdge(0, 4, 14)
g.addEdge(1, 0, 15)
g.addEdge(1, 3, 9)
g.addEdge(1, 4, 2)
g.addEdge(1, 6, 5)
g.addEdge(2, 0, 8)
g.addEdge(2, 6, 12)
g.addEdge(3, 1, 9)
g.addEdge(3, 6, 13)
g.addEdge(3, 5, 11)
g.addEdge(4, 0, 14)
g.addEdge(4, 1, 2)
g.addEdge(4, 5, 7)
g.addEdge(5, 3, 11)
g.addEdge(5, 4, 7)
g.addEdge(5, 6, 4)
g.addEdge(6, 1, 5)
g.addEdge(6, 2, 12)
g.addEdge(6, 3, 13)
g.addEdge(6, 5, 4)

# Function call
g.KruskalMST()
