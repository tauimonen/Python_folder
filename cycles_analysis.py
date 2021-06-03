"""
The solution checks whether there is a directed cycle in the
network. The code performs a depth search from each node, where
color 1 means that the node is being processed and color 2 means
that the node has been processed. If a node color 1 is received,
the cycle is found.
"""

from collections import defaultdict

class Cycles:
    def __init__(self, n):
        self.graph = defaultdict(list)
        self.n = n

    def add_edge(self, a, b):
        self.graph[a].append(b)
        
    def dfs(self, x):
        if self.color[x] == 1:
            self.found = True
            return
        if self.color[x] == 2:
            return
        self.color[x] = 1
        for y in self.graph[x]:
            self.dfs(y)
        self.color[x] = 2

    def check(self):
        self.color = [0] * (self.n + 1)
        self.found = False
        for x in range(1, self.n + 1):
            if self.color[x] == 0:
                self.dfs(x)
        return self.found


if __name__ == "__main__":
    c = Cycles(4)
    c.add_edge(1,2)
    c.add_edge(2,3)
    c.add_edge(1,3)
    c.add_edge(3,4)
    print(c.check()) # False
    c.add_edge(4,2)
    print(c.check()) # True