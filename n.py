class UnionFind:
    def __init__(self, n):
        self._n = n + 1
        self._vanhempi = [i for i in range(self._n)]
        self._koko = [1] * self._n

    def _edustaja(self, x):
        while x != self._vanhempi[x]:
            x = self._vanhempi[x]
        return x

    def yhdista(self, a, b):
        a = self._edustaja(a)
        b = self._edustaja(b)
        if a == b:
            return False
        if self._koko[a] < self._koko[b]:
            a, b = b, a
        self._vanhempi[b] = a
        self._koko[a] += self._koko[b]
        return True

    def maara(self):
        komponentit = set()
        for i in range(1, self._n):
            komponentit.add(self._edustaja(i))
        return len(komponentit)


class PVP:
    def __init__(self, n):
        self._n = n
        self._tiet = []

    def add_road(self, a, b, x):
        self._tiet.append((x, (a, b)))

    def min_cost(self):
        cost = 0
        uf = UnionFind(self._n)
        for t in sorted(self._tiet):
            if uf.yhdista(t[1][0], t[1][1]):
                cost += t[0]
        return cost if uf.maara() == 1 else -1


if __name__ == "__main__":
    g = PVP(1000)
    for i in range(1, 1000):
        for j in range(1, 1000):
            if i != j and j > i:
                w = min(i, j)
                g.add_road(i, j, w)
    print(g.min_cost())