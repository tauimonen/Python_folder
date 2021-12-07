"""
Smallest spanning tree with Kruskal algorithm
"""

class UF:
    def __init__(self, n):
        self.size = [1] * (n + 1)
        self.link = list(range(0, n + 1))
        self.n = n + 1

    def find(self, x):
        while self.link[x] != x:
            x = self.link[x]
        return x

    def components(self):
        count = set()
        for i in range(1, self.n):
            count.add(self.find(i))
        return len(count)

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return False
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.size[a] += self.size[b]
        self.link[b] = a
        return True


class NewRoads:
    def __init__(self, n):
        self.roads = []
        self.n = n

    def add_road(self, a, b, x):
        self.roads.append((x, a, b))

    def min_cost(self):
        minim_cost = 0
        self.roads.sort()
        union_find = UF(self.n)
        for road in self.roads:
            if union_find.union(road[1], road[2]):
                minim_cost += road[0]
                # print(road[0], "**")
        if union_find.components() != 1:
            return - 1
        return minim_cost


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