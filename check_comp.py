class Graph:

    # init function to declare class variables
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(2, V)]
        self.add_all_edges(self.adj)

    def DFSUtil(self, temp, v, visited):

        # Mark the current vertex as visited
        visited[v] = True

        # Store the vertex to list
        temp.append(v)

        # Repeat for all vertices adjacent
        # to this vertex v
        for i in self.adj[v]:
            if visited[i] == False:
                # Update the list
                temp = self.DFSUtil(temp, i, visited)
        return temp

    # method to add an undirected edge
    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    # Method to retrieve connected components
    # in an undirected graph
    def connectedComponents(self):
        visited = []
        cc = []
        for i in range(self.V):
            visited.append(False)
        for v in range(self.V):
            if visited[v] == False:
                temp = []
                cc.append(self.DFSUtil(temp, v, visited))
        return cc

    def add_all_edges(self, nodes):
        for k in range(1, len(nodes)):
            for i in range(1, len(nodes[k])):
                if nodes[k][i] % i == 0 or i % nodes[k][i] == 0:
                    if nodes[k] not in nodes[i]:
                        self.addEdge(nodes[k][i], i)


# Driver Code
if __name__ == "__main__":
    g = Graph(1000)
    cc = g.connectedComponents()
    print("Following are connected components")
    print(cc)