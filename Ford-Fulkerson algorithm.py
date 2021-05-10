from collections import defaultdict

class Verkko:

    def __init__(self, verkko):
        self.verkko = verkko
        self.n = len(verkko)

    def bfs(self, a, b, vanhempi):
        jono = []
        vierailtu = [False] * self.n
        jono.append(a)
        vierailtu[a] = True

        while jono:
            jonosta = jono.pop(0)
            for x, y in enumerate(self.verkko[jonosta]):
                if not vierailtu[x] and y > 0:
                    jono.append(x)
                    vierailtu[x] = True
                    vanhempi[x] = jonosta

        if vierailtu[b]:
            return True
        else:
            return False

    def ff(self, n, m):
        vanhempi = [-1] * self.n
        maksimivirtaus = 0

        while self.bfs(n, m, vanhempi):
            polku = float("Inf")
            s = m
            while s != n:
                polku = min(polku, self.verkko[vanhempi[s]][s])
                s = vanhempi[s]

        maksimivirtaus += polku
        v = m
        while v != n:
            r = vanhempi[v]
            self.verkko[r][v] -= polku
            self.verkko[v][r] += polku
            v = vanhempi[v]
        return maksimivirtaus


if __name__ == "__main__":
    verkko = [[0, 8, 0, 0, 3, 0],
            [0, 0, 9, 0, 0, 0],
            [0, 0, 0, 0, 7, 2],
            [0, 0, 0, 0, 0, 5],
            [0, 0, 7, 4, 0, 0],
            [0, 0, 0, 0, 0, 0]]

    v = Verkko(verkko)
    x = 0
    y = 5
    print(v.ff(x, y))