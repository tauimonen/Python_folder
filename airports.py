class Airports:
    def __init__(self,n):
        self.neighbours = [[] for _ in range(n + 1)]

        self.n = n

    def add_link(self,a,b):
        self.neighbours[a].append(b)

    def dfs(self, node, vis):
        if vis[node]:
            return
        vis[node] = True

        for n in self.neighbours[node]:
            self.dfs(n, vis)

    def check(self):
        res = True
        for i in range(1, self.n):
            visited = [False] * self.n
            self.dfs(i, visited)
            res = res and False not in visited[1:]
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