class Components:
    def __init__(self,n):
        self.link = list(range(n + 1))
        self.size = [1] * (n + 1)

    def find(self, x):
        while self.link[x] != x:
            x = self.link[x]
        return x

    def add_road(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.size[a] += self.size[b]
        w = self.link[b]
        for i in range(len(self.link)):
            if self.link[i] == w:
                self.link[i] = a

    def count(self):
        diff_links = set()
        for link in self.link:
            if link not in diff_links:
                diff_links.add(link)
        return len(diff_links) - 1  # - {0}


if __name__ == "__main__":
    c = Components(5)
    c.add_road(4, 5)
    print(c.count())
    c.add_road(2, 3)
    print(c.count())

    c.add_road(4, 5)
    print(c.count())
    c.add_road(3, 4)

    print(c.count())
    c.add_road(2, 5)
    c.add_road(4, 5)
    print(c.count())
    c.add_road(3, 4)