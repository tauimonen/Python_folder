"""
Smallest spanning tree with Kruskal algorithm
"""

class NewRoads:
    def __init__(self, n):
        self.size = [1] * (n + 1)
        self.link = list(range(0, n + 1))
        self.n = n
        self.roads = []

    def add_road(self, a, b, x):
        self.roads.append((x, a, b))

    def find(self, x):
        while self.link[x] != x:
            x = self.link[x]
        return x

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.size[a] += self.size[b]
        self.link[b] = a

    def min_cost(self):
        cost = 0
        count = self.n
        self.roads.sort()
        for road in sorted(self.roads):
            if self.find(road[1]) and self.find(road[2]):
                self.union(road[1], road[2])
                cost += road[0]
                count -= 1

        return cost if count == 1 else -1


if __name__ == "__main__":
    n = NewRoads(4)
    n.add_road(1,2,2)
    n.add_road(1,3,5)
    print(n.min_cost()) # -1
    n.add_road(3,4,4)
    print(n.min_cost()) # 11
    n.add_road(2,3,1)
    print(n.min_cost()) # 7
    print("="*20)
    n2 = NewRoads(5)
    print(n2.min_cost())
    n2.add_road(3, 5, 7)
    print(n2.min_cost())
    print(n2.min_cost())
    n2.add_road(3, 4, 6)
    print(n2.min_cost())
    n2.add_road(4, 5, 4)
    n2.add_road(1, 2, 7)
    n2.add_road(1, 3, 4)
    print(n2.min_cost()) # 21