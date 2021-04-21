class BestRoute:
    def __init__(self, n):
        self.n = n
        self.verkko = []

    def add_road(self, a, b, x):
        self.verkko.append([a, b, x])
        self.verkko.append([b, a, x])

    def find_route(self, a, b):
        etaisyys = [float("Inf")] * (self.n + 1)
        etaisyys[a] = 0
        for _ in range(0, self.n - 1):
            for u, v, w, in self.verkko:
                if etaisyys[u] != float("Inf") and etaisyys[u] + w < etaisyys[v]:
                    etaisyys[v] = etaisyys[u] + w

        if etaisyys[b] == float("Inf"):
            return -1
        return etaisyys[b]


if __name__ == "__main__":
    b = BestRoute(3)
    b.add_road(1, 2, 2)
    print(b.find_route(1, 3))  # -1
    b.add_road(1, 3, 5)
    print(b.find_route(1, 3))  # 5
    b.add_road(2, 3, 1)
    print(b.find_route(1, 3))  # 3
