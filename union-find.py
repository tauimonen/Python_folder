n = 10

link = list(range(n + 1))
size = [1] * (n+1)

def find(x):
    while link[x] != x:
        x = link[x]
    return x

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return
    if size[a] < size[b]:
        a, b = b, a
    size[a] += size[b]
    link[b] = a








