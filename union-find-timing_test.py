"""
Luokka union-find -toteutuksen testaukseen.
"""
from random import randint

class UF:
    def __init__(self, n):
        self.n = n
        self.link = list(range(n + 1))
        self.size = [1] * (n+1)

    def find(self, x):
        while self.link[x] != x:
            x = self.link[x]
        return x

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.size[a] += self.size[b]
        self.link[b] = a

    def test(self, n):
        """
        Yhdistää verkon komponentteja satunnaisesti ja tulostaa
        jäljelle jäävien komponenttien määrän n:n toiston jälkeen.
        :param n: Int
        """
        setti = set()
        for i in range(n):
            a = randint(0, n - 1)
            b = randint(0, n - 1)
            graph.union(a, b)
        for link in graph.link:
            setti.add(link)
        component_count = len(setti)
        print(f"Komponenttien määrä kun n = {n}: {component_count}")


if __name__ == "__main__":
    from timeit import time

    # Testien ajastus n:n arvoilla 100, 1000, 10000 ja 10000

    n = 100
    print(50 * "=")
    t0 = time.time()
    graph = UF(n)
    graph.test(n)
    t1 = time.time()
    print(f"Suoritukseen kulunut aika: {t1 - t0}")
    print(50 * "=")

    n = 1000
    t0 = time.time()
    graph = UF(n)
    graph.test(n)
    t1 = time.time()
    print(f"Suoritukseen kulunut aika: {t1 - t0}")
    print(50 * "=")

    n = 10000
    t0 = time.time()
    graph = UF(n)
    graph.test(n)
    t1 = time.time()
    print(f"Suoritukseen kulunut aika: {t1 - t0}")
    print(50 * "=")

    n = 100000
    t0 = time.time()
    graph = UF(n)
    graph.test(n)
    t1 = time.time()
    print(f"Suoritukseen kulunut aika: {t1 - t0}")
    print(50 * "=")





