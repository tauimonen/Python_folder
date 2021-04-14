class Coloring:
    def __init__(self, n):
        self.n = n
        self.graph = {}
        for i in range(1, n + 1):
            self.graph[i] = []
        self.possible = True

    def add_edge(self, a, b):
        self.graph[a].append(b)
        self.graph[b].append(a)

    def check(self):
        print(self.graph)
        red = set()
        blue = set()
        turn = 0
        for q in range(1, self.n + 1):
            print("alussa")
            node = q
            if node not in blue and node not in red:
                print("red: ", red, "blue: ", blue)
                print("Lisätään punaiseen: ", node)
                red.add(node)
            queue = []
            queue.append(node)
            while queue:
                s = queue.pop(0)
                print("uusi s: ", s)
                for neighbour in self.graph[s]:
                    if neighbour in red and s in red or neighbour in blue and s in blue:
                        self.possible = False
                    else:
                        if s in blue:
                            red.add(neighbour)
                            print("Lisätään punaiseen: ", neighbour)
                        if s in red:
                            blue.add(neighbour)
                            print("Lisätään siniseen: ", neighbour)
                        if neighbour not in blue and neighbour not in red:
                            queue.append(neighbour)

            turn += 1
            if turn >= self.n:
                break
        return self.possible


if __name__ == "__main__":
    # c = Coloring(4)
    # c.add_edge(1, 2)
    # c.add_edge(2, 3)
    # c.add_edge(3, 4)
    # c.add_edge(1, 4)
    # print(c.check())  # True
    # c.add_edge(2, 4)
    # print(c.check())  # False

    c = Coloring(5)
    c.add_edge(4, 5)
    c.add_edge(2, 3)
    c.add_edge(3, 5)
    c.add_edge(1, 3)
    print(c.check())

