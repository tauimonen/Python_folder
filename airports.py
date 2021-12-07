class Airports:
    def __init__(self,n):
        self._n = n + 1
        self._neighbors = [[] for _ in range(self._n)]

    def add_link(self,a,b):
        self._neighbors[a].append(b)

    def _dfs(self, node, visited):
        if visited[node]:
            return
        visited[node] = True
        for i in self._neighbors[node]:
            self._dfs(i, visited)

    def check(self):
        res = True
        for i in range(0, self._n):
            visited = [False]*self._n
            self._dfs(i, visited)
            res = res and False not in visited
        return res



if __name__ == "__main__":
    a = Airports(5)
    a.add_link(1,2)
    a.add_link(2,3)
    a.add_link(1,3)
    a.add_link(4,5)
    print(a.check()) # False
    a.add_link(3,5)
    a.add_link(1,4)
    print(a.check()) # False
    a.add_link(5,1)
    print(a.check()) # True

    a2 = Airports(5)
    a2.add_link(3, 1)
    a2.add_link(3, 4)
    a2.add_link(3, 4)
    a2.add_link(5, 2)
    a2.add_link(4, 3)
    a2.add_link(5, 2)
    a2.add_link(4, 5)
    a2.add_link(3, 5)
    a2.add_link(3, 2)
    print(a2.check()) # False

    a3 = Airports(5)
    a3.add_link(1, 4)
    a3.add_link(2, 3)
    a3.add_link(5, 3)
    a3.add_link(3, 2)
    a3.add_link(5, 4)
    a3.add_link(3, 5)
    a3.add_link(4, 1)
    a3.add_link(5, 4)
    a3.add_link(5, 4)
    print(a.check()) # False