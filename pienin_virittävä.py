class PVP:
    def __init__(self, n):
        self.n = n
        self.graph = []

    def add_road(self, u, v, w):
        self.graph.append([u, v, w])

    def print(self):
        print(self.graph)

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
        i = 0
        e = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = []
        rank = []
        for node in range(self.n):
            parent.append(node)
            rank.append(0)
        while e < self.n - 1:
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


if __name__ == "__main__":
    g = PVP(1001)
    for i in range(1, 1001):
        for j in range(1, 1001):
            if i != j and j > i:
                w = min(i, j)
                g.add_road(i, j, w)

    g.print()
    print(g.kruskal())

