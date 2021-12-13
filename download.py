from collections import defaultdict

class Download:
    """
    Class for calculating the maximum amount of data that can be transmitted
    from a given computer to another in a second in a given network.
    Using Ford-Fulkerson and breadth-first search.
    """
    def __init__(self,n):
        self.n = n + 1
        self.graph = [[0] * (n + 1) for _ in range(self.n)]

    def add_link(self, a, b, x):
        self.graph[a][b] += x

    def bfs(self, a, b, v):
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
                    v[x] = jonosta

        if vierailtu[b]:
            return True
        return False

    def calculate(self,a,b):
        maxim = 0
        v = [-1] * self.n
        while self.bfs(a, b, v):
            flow = 10**9
            n = b
            while n != a:
                flow = min(flow, self.graph[v[n]][n])
                n = v[n]
            maxim += flow
            x = b
            while x != a:
                y = v[x]
                self.graph[y][x] -= flow
                self.graph[x][y] += flow
                x = v[x]
        return maxim


if __name__ == "__main__":
    d = Download(5)
    print(d.calculate(3, 4))
    d.add_link(5, 3, 6)
    print(d.calculate(5, 4))
    print(d.calculate(4, 5))
    print(d.calculate(5, 1))
    d.add_link(5, 4, 9)
    d.add_link(1, 2, 10)
    print(d.calculate(3, 1))
    print(d.calculate(2, 4))
    print(d.calculate(5, 4))
    d.add_link(5, 2, 9)
    print(d.calculate(1, 5)) # 13
    d.add_link(3, 5, 2)
    d.add_link(1, 3, 2)
    d.add_link(5, 4, 9)
    print(d.calculate(5, 4))
    print(d.calculate(2, 3))
    print(d.calculate(1, 3))
    print(d.calculate(3, 2))
    print(d.calculate(5, 4))
    print(d.calculate(4, 5))
    d.add_link(4, 3, 9)
    print(d.calculate(4, 5))
    print(d.calculate(2, 4))
    print(d.calculate(4, 5))
    d.add_link(5, 1, 6)
    d.add_link(3, 5, 3)
    d.add_link(4, 5, 2)
    print(d.calculate(3, 4))
    d.add_link(5, 3, 3)