class Download:
    def __init__(self,n):
        self.n = n + 1
        self.graph = [[0] * (n + 1) for _ in range(self.n)]

    def add_link(self, a, b, x):
        self.graph[a][b] += x

    def bfs(self, a, b, vanhempi):
        jono = []
        vierailtu = [False] * self.n
        jono.append(a)
        vierailtu[a] = True

        while jono:
            jonosta = jono.pop(0)
            for x, y in enumerate(self.graph[jonosta]):
                if not vierailtu[x] and y > 0:
                    jono.append(x)
                    vierailtu[x] = True
                    vanhempi[x] = jonosta

        if vierailtu[b]:
            return True
        else:
            return False



    def calculate(self,a,b):
        vanhempi = [-1] * self.n
        maksimivirtaus = 0

        while self.bfs(a, b, vanhempi):
            polku = float("Inf")
            s = b
            while s != a:
                polku = min(polku, self.graph[vanhempi[s]][s])
                s = vanhempi[s]

        maksimivirtaus += polku
        v = b
        while v != a:
            r = vanhempi[v]
            self.graph[r][v] -= polku
            self.graph[v][r] += polku
            v = vanhempi[v]
        return maksimivirtaus


if __name__ == "__main__":
    d = Download(4)
    print(d.calculate(1,4)) # 0
    d.add_link(1,2,5)
    d.add_link(2,4,6)
    d.add_link(1,4,2)
    print(d.calculate(1,4)) # 7
    d.add_link(1,3,4)
    d.add_link(3,2,2)
    print(d.calculate(1,4)) # 8