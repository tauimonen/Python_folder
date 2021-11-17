from collections import deque

class Components:
    def __init__(self, n):
        self.nodes = {}
        for i in range(2, n+1):
            self.nodes[i] = []
        self.add_all_edges(self.nodes)

    def add_edge(self, a, b):
        self.nodes[a].append(b)
        self.nodes[b].append(a)

    def add_all_edges(self, nodes):
        for node in nodes:
            for i in range(2, len(nodes)):
                if node % i == 0 or i % node == 0:
                    if node not in nodes[i]:
                        self.add_edge(node, i)

    def print_network(self):
        for i in range(1, len(self.nodes)):
            print(i, "=", self.nodes[i])

    def find_component_count(self):
        unvisited = set(range(2, len(self.nodes)))
        component_count = 0
        queue = deque()
        while len(unvisited) > 0:
            component_count += 1
            node = next(iter(unvisited))
            unvisited.remove(node)
            queue.append(node)
            while len(queue) > 0:
                node = queue.popleft()
                for neighbour in self.nodes[node]:
                    if neighbour in unvisited:
                        unvisited.remove(neighbour)
                        queue.append(neighbour)
        return component_count


if __name__ == "__main__":
    c = Components(1000)
    count = c.find_component_count()
    print("Component count in the network is", count)