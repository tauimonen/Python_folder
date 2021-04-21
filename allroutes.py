class AllRoutes:
    def __init__(self, n):
        self.n = n
        self.verkko = [[float("inf") for _ in range(self.n)] for _ in range(self.n)]

    def add_road(self, a, b, x):
        if x < self.verkko[a - 1][b - 1]:
            self.verkko[a - 1][b - 1] = x
            self.verkko[b - 1][a - 1] = x

    def get_table(self):
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    self.verkko[i][j] = min(self.verkko[i][j], self.verkko[i][k] + self.verkko[k][j])
        for i in range(self.n):
            for j in range(self.n):
                if j == i:
                    self.verkko[i][j] = 0
                elif self.verkko[i][j] == float("inf"):
                    self.verkko[i][j] = -1
        return self.verkko


if __name__ == "__main__":
    a = AllRoutes(5)
    a.add_road(3, 4, 6)
    a.add_road(4, 5, 5)
    a.add_road(4, 5, 6)
    a.add_road(1, 5, 7)
    a.add_road(1, 4, 7)
    a.add_road(4, 5, 1)
    a.add_road(3, 4, 8)
    a.add_road(2, 3, 6)
    a.add_road(4, 5, 4)
    print(a.get_table())
    # [[0, 19, 13, 7, 7], [19, 0, 6, 12, 13], [13, 6, 0, 6, 7], [7, 12, 6, 0, 1], [7, 13, 7, 1, 0]]
