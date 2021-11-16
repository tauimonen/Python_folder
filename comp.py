class Components:
    def __init__(self, n):
        self.nodes = {}
        for i in range(1, n+1):
            self.nodes[i] = []
        self.add_all_edges(self.nodes)

    def add_edge(self, a, b):
        self.nodes[a].append(b)
        self.nodes[b].append(a)

    def add_all_edges(self, nodes):
        for node in nodes:
            for i in range(1, len(nodes)):
                if node % i == 0 or i % node == 0:
                    if node not in nodes[i]:
                        self.add_edge(node, i)

    def print_network(self):
        for i in range(1, len(self.nodes)):
            print(i, "=", self.nodes[i])


if __name__ == "__main__":
    c = Components(1000)
    c.print_network()