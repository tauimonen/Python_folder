class NewRoads:

    def __init__(self, n):
        self.n = n
        self.graph = []
        self.link = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find(self, x):
        while self.link[x] != x:
            x = self.link[x]
        return x

    def add_road(self, a, b, w):
        self.graph.append([a-1, b-1, w])
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.size[a] += self.size[b]
        w = self.link[b]
        for i in range(len(self.link)):
            if self.link[i] == w:
                self.link[i] = a

    def union(self, parent, rank, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def count(self):
        diff_links = set()
        for link in self.link:
            if link not in diff_links:
                diff_links.add(link)
        return len(diff_links) - 1  # - {0}

    def min_cost(self):
        result = []
        link = []
        rank = []
        i = 0
        e = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        while e < self.n - 1 and i <= self.n - 1:
            print(self.count())
            if self.count() != 1:
                return -1  # if there's no possible way to connect all
            print(i, self.graph)
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(u)
            y = self.find(v)
            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(link, rank, x, y)
        minimum = 0
        for u, v, weight in result:
            minimum += weight
        return minimum


# n = NewRoads(4)
# n.add_road(1, 2, 2)
# n.add_road(1, 3, 5)
# print(n.min_cost())  # -1
# n.add_road(3, 4, 4)
# print(n.min_cost())  # 11
# n.add_road(2, 3, 1)
# print(n.min_cost())  # 7
#
# n = NewRoads(5)
# print(n.min_cost())
# n.add_road(3, 5, 7)
# print(n.min_cost())
# print(n.min_cost())
# n.add_road(3, 4, 6)
# print(n.min_cost())
# n.add_road(4, 5, 4)
# n.add_road(1, 2, 7)
# n.add_road(1, 3, 4)
# print(n.min_cost())

n = NewRoads(5)
n.add_road(4,5,2)
n.add_road(2,3,4)
n.add_road(1,2,10)
print(n.min_cost())
print(n.min_cost())
print(n.min_cost())
print(n.min_cost())
print(n.min_cost())
n.add_road(2,4,2)
print(n.min_cost())