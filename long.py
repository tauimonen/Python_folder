class LongPath:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n + 1)]

    def add_edge(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)

    def longest(self, x):
        if x in self.memory:
            return self.memory[x]
        length = 0
        for y in self.graph[x]:
            if y > x:
                length = max(length, self.longest(y) + 1)
        self.memory[x] = length
        return length

    def calculate(self):
        self.memory = {}
        result = 0
        for i in range(1, self.n + 1):
            print(self.memory)
            result = max(result, self.longest(i))
        return result


if __name__ == "__main__":
    l = LongPath(4)
    l.add_edge(1, 2)
    l.add_edge(1, 3)
    l.add_edge(2, 4)
    l.add_edge(3, 4)
    print(l.calculate())    # 2
    l.add_edge(3, 2)
    print(l.calculate())    # 3