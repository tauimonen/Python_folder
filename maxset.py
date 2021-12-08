class MaxSet:
    def __init__(self,n):
        self.size = [1] * (n + 1)
        self.link = list(range(0, n + 1))
        self.n = n + 1
        self.count = 1

    def find(self, x):
        while self.link[x] != x:
            x = self.link[x]
        return x

    def merge(self,a,b):
        a = self.find(a)
        b = self.find(b)
        if a == b: return
        if self.size[a] < self.size[b]:
            a, b = b, a
        self.size[a] += self.size[b]
        if self.size[a] > self.count:
            self.count = self.size[a]
        self.link[b] = a


    def get_max(self):

        res = self.count
        return res


if __name__ == "__main__":
    m = MaxSet(5)
    print(m.get_max()) # 1
    m.merge(1,2)
    m.merge(3,4)
    m.merge(3,5)
    print(m.get_max()) # 3
    m.merge(1,5)
    print(m.get_max()) # 5