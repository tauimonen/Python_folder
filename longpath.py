class LongPath:
    def __init__(self,n):
        self.n = n
        self.und_graph = [[] for _ in range(0, n + 1)]
        self.visited = {}
        self.distances = [0] * n

    def add_edge(self,a,b):
        self.und_graph[a].append(b)
        self.und_graph[b].append(a)

    def dfs(self, node):
        if self.visited[node] == 2:
            return
        if self.visited[node] == 1:
            return

        self.visited[node] = 1
        for neighbour in self.und_graph[node]:
            self.dfs(neighbour)
        self.visited[node] = 2

        self.sorted.append(node)


    def calculate(self):
        self.sorted = []
        visited = [0] * self.n
        for i in range(1, self._):
            if visited[i] == 0:
                self.dfs(i, visited, sorted)
        sorted.reverse()

        # 2. lasketaan pisin polku jokaiseen solmuun
        distances = [0] * self._n
        for v in sorted:
            if len(self._predecessors[v]) > 0:
                distances[v] = max([distances[i] + 1 for i in self._predecessors[v]])

        # 3. palautetaan pisin kaikista poluista
        return max(distances)


if __name__ == "__main__":
    l = LongPath(4)
    l.add_edge(1,2)
    l.add_edge(1,3)
    l.add_edge(2,4)
    l.add_edge(3,4)
    print(l.calculate()) # 2
    l.add_edge(3,2)
    print(l.calculate()) # 3