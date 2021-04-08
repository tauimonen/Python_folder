class Cities:
    def __init__(self, n):
        self.cities = {}
        for i in range(1, n+1):
            self.cities[i] = []

    def add_road(self, a, b):
        self.cities[a].append(b)
        self.cities[b].append(a)

    def has_route(self, a, b):
        visited = []
        queue = []
        visited.append(a)
        queue.append(a)
        while queue:
            s = queue.pop(0)
            if s == b:
                return True
            for neighbour in self.cities[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
        return False



