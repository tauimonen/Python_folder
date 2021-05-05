class NewRoads:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = []

    def add_road(self, u, v, w):
        self.graph.append([u, v, w])

    def search(self, parent, i):
        if parent[i] == i:
            return i
        return self.search(parent, parent[i])

    def apply_union(self, parent, rank, x, y):
        xroot = self.search(parent, x)
        yroot = self.search(parent, y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1


    def kruskal(self):
        result = []
        total_weight = 0
        i, e = 0, 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.V):
            parent.append(node)
            rank.append(0)
        while e < self.V - 1:
            if i < len(self.graph):
                u, v, w = self.graph[i]
            else:
                return - 1
            i = i + 1
            x = self.search(parent, u)
            y = self.search(parent, v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.apply_union(parent, rank, x, y)
        for u, v, weight in result:
            print("Edge:", u, v, end=" ")
            print("-", weight)
            total_weight += weight
        return total_weight



if __name__ == "__main__" :
    n = NewRoads(5)
    n.add_road(1, 2, 2)
    n.add_road(1, 3, 5)
    print(n.kruskal())  # -1
    n.add_road(3, 4, 4)
    print(n.kruskal())  # 11
    n.add_road(2, 3, 1)
    print(n.kruskal()) # 7



